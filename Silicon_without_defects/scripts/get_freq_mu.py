import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import math 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


def calculate_thermal_diffusivity(thermal_conductivity, density, specific_heat_capacity):
    alpha= thermal_conductivity / (density * specific_heat_capacity)
    return alpha

def modulation_frequency(alpha, thermal_diffusion_length):
    return alpha / (math.pi * thermal_diffusion_length**2)

def thermal_diffusion_length(freq, thermal_diffusivity):
    mu= np.sqrt(thermal_diffusivity/np.pi*freq)
    return mu

if __name__ == "__main__":
    sample_mat= np.array ([148, 2330,710])
    sample_mat= sample_mat.reshape((1,3))
    thermal_conductivity = sample_mat[0,0]
    density = sample_mat[0,1]
    specific_heat_capacity = sample_mat[0,2]
    thermal_diffusivity = calculate_thermal_diffusivity(thermal_conductivity, density, specific_heat_capacity)
    thermal_diffusion_length(1.5, thermal_diffusivity)