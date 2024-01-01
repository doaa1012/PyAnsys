from ansys.mapdl.core import launch_mapdl
import numpy as np
import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)
import pandas as pd
import pickle
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from scripts.defects_loc import define_defects
from config import *

def simulate_heat_transfer(freq, Temp_Path, Loc_Path ):
    mapdl = launch_mapdl()
    mapdl.clear()
    sample_dim= np.array([50e-3, 50e-3,4e-3])
    sample_mat= np.array ([148, 2330,710])
    sample_dim= sample_dim.reshape((1,3))
    sample_mat= sample_mat.reshape((1,3))

    sample_x = sample_dim[0,0]
    sample_y = sample_dim[0, 1]
    sample_z = sample_dim[0,2]

    kxx= sample_mat[0,0]
    dens = sample_mat[0,1]
    c= sample_mat[0,2]

    Q = 1000
    #freq = 1
    T_wave = 1 / freq  
    omega = 2 * np.pi * freq  
    t_end = 250 * T_wave 
    print(t_end)
    room_temp = 25
    num_steps=100
    time_values = np.linspace(0, t_end, num_steps, endpoint=False)
    cos_values = np.cos(omega * time_values)
    heat_flux = Q * (1 - cos_values)

    # Store time and heat_flux in the load_table
    load_table = np.column_stack((time_values, heat_flux))
    frame_rate= 50
    t_step = 1/ frame_rate
    delta_x = np.sqrt((t_step * 2 * kxx) / (dens * c))

    mapdl.clear()
    mapdl.prep7()

    mapdl.et(1,70)
    mapdl.mp(lab="KXX", mat=1 , c0=kxx)
    mapdl.mp(lab='DENS', mat=1, c0=dens)
    mapdl.mp(lab='C', mat=1, c0=c)

    # creating the geometry
    rect_vol = mapdl.block(0, sample_x, 0, sample_y, 0, sample_z)
    mapdl.allsel()
    mapdl.esize(size=delta_x)
    mapdl.vsweep(vnum=rect_vol)
    mapdl.mshape(1, "3D")
    mapdl.mshkey(0)
    mapdl.vmesh("all")
    #mesh = pv.Plane(i_resolution=100, j_resolution=100)
    #mesh.plot(color="w", show_edges=True)
    mapdl.vplot()

    mapdl.nsel("S", "LOC","z", vmin=sample_z, vmax=sample_z)
    top_surf_nodes = mapdl.mesh.nnum

    # Solution
    mapdl.slashsolu()
    mapdl.allsel()

    mapdl.load_table("load_table", load_table, "TIME")
    mapdl.outres('ERASE')
    mapdl.outres('ALL', 'ALL')

    mapdl.antype(4)
    mapdl.trnopt("Full")  

    mapdl.kbc(0)
    mapdl.allsel("All")
    mapdl.tunif(room_temp)


    # applying heat flux on the top surface
    mapdl.asel(type_='S', item='LOC', comp='Z', vmin= sample_z,  vmax=sample_z)
    mapdl.nsel(type_='S', item='LOC', comp='Z', vmin=sample_z)
    mapdl.sf(nlist="All", lab="conv", value=20, value2=room_temp)
    mapdl.sfa(area= "ALL", lab="HFLUX", value='%load_table%')
    mapdl.time(t_end)
    mapdl.timint('ON')


    mapdl.deltim(t_step,t_step, t_step)
    mapdl.autots('OFF')

    mapdl.allsel("All")
    mapdl.solve()
    mapdl.finish()

    # post processing 

    mapdl.post1()
    node_temp_from_post_top = {}
    time_values = mapdl.post_processing.time_values
    mapdl.post_processing.plot_nodal_temperature()

    # Loop through each time step and get temperatures for each node in 'top_surf_nodes'
    for i, t in enumerate(time_values):
        mapdl.set(1, i + 1)  # Set the result number to the current index 'i'
        node_temp_from_post_top[t] = []  # Initialize the list for the current time step
        for n in top_surf_nodes:
            node_temp_from_post_top[t].append(round(mapdl.get_value("node", n, "TEMP"),4) )

    print("Done_Temperature")
    # saving the x,y,z coordinates.
    nodes_loc = {}
    for n in top_surf_nodes:
        x = mapdl.queries.nx(n)
        y = mapdl.queries.ny(n)
        z = mapdl.queries.nz(n)
        nodes_loc[n] = [x, y, z]

    print("Done_Nodes")

    print(freq)
    print(mapdl.nsel("all").shape)
    print(mapdl.queries.node(10e-3,0,0), "Sound")
    print(mapdl.queries.node(12e-3,12e-3,0), "Defect_node")
    # Save data using frequency in the filename
    grid = mapdl.mesh.grid
    grid.save('my_mesh.vtk')
    frequency_str = str(freq).replace('.', '_')  # Convert frequency to a valid filename
    pickle_file_temp = f"dict_temp_{frequency_str}.p"
    pickle_file_nodes = f"nodes_loc_{frequency_str}.p"
    
    pickle_file_temp_path = os.path.join(Temp_Path, pickle_file_temp)
    pickle_file_nodes_path = os.path.join(Loc_Path, pickle_file_nodes)

    with open(pickle_file_temp_path , 'wb') as pickle_file:
        pickle.dump(node_temp_from_post_top, pickle_file)

    with open(pickle_file_nodes_path, 'wb') as pickle_file:
        pickle.dump(nodes_loc, pickle_file)
    print("Done")
    mapdl.exit()
if __name__ == "__main__":
    simulate_heat_transfer(4)
    #Done_Temperature
    #Done_Nodes
    #(8120,)
    #3014
    #3013
    #Done