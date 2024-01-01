import matplotlib.pyplot as plt
import pickle
from ansys.mapdl.core import launch_mapdl
import numpy as np
import os
import time
import pyvista as pv
from define_geometry import define_geometry


def get_solution(freq= 10, power=100, sample_x=50e-3,sample_y=50e-3 ):
    define_geometry()

    mapdl = launch_mapdl()
    mapdl.slashsolu()
    mapdl.allsel()
    room_temp= 25
    area = sample_x * sample_y
    powerdens = power/area
    


    mapdl.antype(3)  
    mapdl.harfrq(freqb=0,freqe=freq)
    mapdl.nsubst(nsbstp=10)
    
    mapdl.kbc(0) 
    mapdl.autots('OFF')

    mapdl.asel("S","loc","z", 0)
    mapdl.tunif(temp=room_temp)

    mapdl.outres('ERASE')
    mapdl.outres('ALL', 'ALL')
    
    mapdl.nropt("Full")
    

    #mapdl.nsel(type_='S', item='LOC', comp='Z', vmin=-4e-3)
    #mapdl.sf(nlist="All", lab="conv", value=20, value2=room_temp)

    mapdl.asel(type_='S', item='LOC', comp='Z', vmin=0)
    mapdl.sfa(area= "ALL", lab="HFLUX", value=powerdens)

    mapdl.allsel("All")
    mapdl.solve()
    print("done")
    mapdl.finish()
    print("done")



if __name__ == "__main__":
    get_solution()