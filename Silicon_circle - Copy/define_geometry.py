import matplotlib.pyplot as plt
import pickle
from ansys.mapdl.core import launch_mapdl
import numpy as np
import os
import time
import pyvista as pv

def define_geometry():

    mapdl = launch_mapdl()

    sample_dim= np.array([180e-3, 180e-3,-10e-3])
    sample_mat= np.array([16.2, 7900 , 477])
    sample_dim= sample_dim.reshape((1,3))
    sample_mat= sample_mat.reshape((1,3))

    sample_x = sample_dim[0,0]
    sample_y = sample_dim[0, 1]
    sample_z = sample_dim[0,2]

    kxx= sample_mat[0,0]
    dens = sample_mat[0,1]
    c= sample_mat[0,2]

    Q = 1000
    freq = 0.182
    #freq = 1
    T_wave = 1 / freq  
    omega = 2 * np.pi * freq  
    t_end = 5 * T_wave 
    room_temp = 25
    num_steps_per_wave = 10


    #deltim = T_wave / t_end 
    deltim =(0.5* T_wave) / t_end 

    num_steps = int(t_end / deltim)
    time_values = np.linspace(0, t_end, num_steps, endpoint=False)
    cos_values = np.cos(omega * time_values)
    heat_flux = Q * (1 - cos_values)

    # Store time and heat_flux in the load_table
    load_table = np.column_stack((time_values, heat_flux))


    # Plot the cosine function
    plt.plot(time_values, heat_flux)
    plt.xlabel('Time')
    plt.ylabel('Heat Flux')
    plt.title('Heat Flux vs. Time')
    plt.grid(False)
    #plt.show()
    plt.savefig('input.png')

    delta_x = np.sqrt((deltim * 10 * kxx) / (dens * c))

    mapdl.clear()
    mapdl.prep7()

    mapdl.et(1,70)
    mapdl.mp(lab="KXX", mat=1 , c0=kxx)
    mapdl.mp(lab='DENS', mat=1, c0=dens)
    mapdl.mp(lab='C', mat=1, c0=c)

    # creating the geometry
    rect_vol = mapdl.block(0, sample_x, 0, sample_y, 0, sample_z)
    num_defects = 5

    for i in range(1, num_defects):
        x_increment=40e-3
        x_coord = i * x_increment
        radius = 8e-3 -i * 1e-3  # Adjust the radius based on your requirement
        depth = -5e-3 + i * 1e-3   # Adjust the depth based on your requirement

        cly_complete = mapdl.cyl4(xcenter=x_coord, ycenter=40e-3, rad1=radius, depth=sample_z)
        cly_partial = mapdl.cyl4(xcenter=x_coord, ycenter=40e-3, rad1=radius, depth=depth)

        mapdl.vsel('none')
        mapdl.vsel('A', vmin=rect_vol)
        mapdl.vsel('A', vmin=cly_complete)
        mapdl.vsbv(nv1=rect_vol, nv2=cly_complete)
        mapdl.allsel()
        mapdl.vglue("all")

    #mapdl.vplot("all")  

    mapdl.allsel()
    mapdl.esize(size=delta_x*10)
    mapdl.vsweep(vnum=rect_vol)
    mapdl.mshape(1, "3D")
    mapdl.mshkey(0)
    mapdl.vmesh("all")

    mapdl.nsel("S", "LOC","z", vmin=0, vmax=0)
    top_surf_nodes = mapdl.mesh.nnum
    print("done")

if __name__ == "__main__":
    define_geometry()

