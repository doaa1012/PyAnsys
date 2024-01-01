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

from config import *

def fourier_analysis(loaded_node_temp, f):
    pi = np.arccos(-1)
    #f = 1
    # Create a dictionary of temperature data, where keys are time steps and values are temperature arrays
    # Replace this with your actual data
    temperature_data = loaded_node_temp

    # Determine the number of time steps and nodes
    timesteps = len(temperature_data)
    nodecount = len(next(iter(temperature_data.values())))

    # Initialize arrays for calculations
    temptab0 = np.zeros((nodecount, timesteps))
    temptab90 = np.zeros((nodecount, timesteps))
    signal0 = np.zeros(nodecount)
    signal90 = np.zeros(nodecount)

    # Loop through time steps
    for i, currenttime in enumerate(temperature_data.keys()):
        ntemp = temperature_data[currenttime]
        ntemp = np.array(ntemp)

        K0 = 2 * np.sin(2 * pi * f * currenttime - pi / 2)
        K90 = 2 * np.cos(2 * pi * f * currenttime - pi / 2)
        
        temptab0[:, i] = ntemp * K0
        temptab90[:, i] = ntemp * K90

    # Perform transpose for the arrays
    temptab0t = temptab0.T
    temptab90t = temptab90.T

    # Calculate signal0 and signal90
    signal0 = np.sum(temptab0t, axis=0) / timesteps
    signal90 = np.sum(temptab90t, axis=0) / timesteps

    # Calculate s02, s902, s02S902, and amplitude
    s02 = signal0 * signal0
    s902 = signal90 * signal90

    amplitude_DFT = np.sqrt(s02 + s902)

    phase_DFT = np.arctan2(signal90, signal0)

    return amplitude_DFT, phase_DFT

def numerical_equation(P, f):
    
    specific_heat = 700.0  
    density = 2329.0  
    thermal_conductivity = 150.0  
    omega = 2 * np.pi*f
    e= specific_heat * density * thermal_conductivity
    Amplitude = P /(np.sqrt( specific_heat * density * thermal_conductivity* omega))

    # Print the result
    print(f"Temperature Amplitude = {Amplitude:.5f} degrees Celsius")

    return Amplitude