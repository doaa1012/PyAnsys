import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from scripts.plot_images import plot_images
import matplotlib.patches as patches
from scripts.get_freq_mu import *

def get_depth(freq, loc, phase , fixed_y=0.01, fixed_x=0.01, rect_size=3, margin=1, label="Temperature"):
    
    grid_temperature, x_min, x_max, y_min, y_max, grid_x, grid_y = plot_images(phase, loc, label=label, plot_image=False)
    x_index = np.argmin(np.abs(grid_x[0, :] - fixed_x))
    y_index = np.argmin(np.abs(grid_y[:, 0] - fixed_y))


    # Define the size of the rectangular regions
    x_range_center = (int(x_index - rect_size), int(x_index + rect_size))
    y_range_center = (int(y_index - rect_size), int(y_index + rect_size))

    x_range_nearby = (int(x_index - rect_size-margin), int(x_index + rect_size+margin))
    y_range_nearby = (int(y_index - rect_size-margin), int(y_index + rect_size+margin))

    # Extracting the rectangular regions of the grid_temperature
    rectangular_region_center = grid_temperature[y_range_center[0]:y_range_center[1], x_range_center[0]:x_range_center[1]]
    rectangular_region_nearby = grid_temperature[y_range_nearby[0]:y_range_nearby[1], x_range_nearby[0]:x_range_nearby[1]]
    values_not_in_center = np.setdiff1d(rectangular_region_nearby, rectangular_region_center)
    

    #if label=="phase":
    center_row = rectangular_region_center.shape[0] // 2
    center_col = rectangular_region_center.shape[1] // 2
    center_index_nearby = values_not_in_center.shape[0] // 2

    center_value_center = rectangular_region_center[center_row, center_col]
    center_value_center_nearby = values_not_in_center[center_index_nearby] 
    phase_difference= abs(center_value_center-center_value_center_nearby)
    sample_mat= np.array ([148, 2330,710])
    sample_mat= sample_mat.reshape((1,3))
    thermal_conductivity = sample_mat[0,0]
    density = sample_mat[0,1]
    specific_heat_capacity = sample_mat[0,2]
    thermal_diffusivity = calculate_thermal_diffusivity(thermal_conductivity, density, specific_heat_capacity)
    mu=thermal_diffusion_length(freq, thermal_diffusivity)
    depth= abs(phase_difference * mu)
    
    return phase_difference,depth