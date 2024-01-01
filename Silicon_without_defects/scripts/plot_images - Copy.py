import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

# ode_temp_from_post_top can be phase or amplitude to plot it.

def plot_images(node_temp_from_post_top, nodes_loc, label="Temperature", plot_image= True):

    x_values_list = []
    y_values_list = []
    z_values_list = []
    # Iterate through the 'nodes_loc' dictionary and extract 'x' values
    for node_id, coordinates in nodes_loc.items():
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]
        z_coordinate = coordinates[2]
        x_values_list.append(x_coordinate)
        y_values_list.append(y_coordinate)
        z_values_list.append(z_coordinate)

    x_values = np.array(x_values_list)
    y_values = np.array(y_values_list)
    z_values = np.array(z_values_list)

    temperature_values = np.array(node_temp_from_post_top)
    x_min, x_max = x_values.min(), x_values.max()
    y_min, y_max = y_values.min(), y_values.max()
    grid_resolution = 100
    grid_x, grid_y = np.linspace(x_min, x_max, grid_resolution), np.linspace(y_min, y_max, grid_resolution)
    grid_x, grid_y = np.meshgrid(grid_x, grid_y)


    grid_temperature = griddata((x_values, y_values), temperature_values, (grid_x, grid_y), method='linear')
    if plot_image == True:
        plt.figure(figsize=(8, 6))
        plt.imshow(grid_temperature, extent=(x_min, x_max, y_min, y_max), cmap="viridis", origin="lower", aspect="auto")
        plt.colorbar(label=label)
        plt.xlabel("X-coordinate")
        plt.ylabel("Y-coordinate")
        plt.axis('off')
        plt.show()

    return grid_temperature,x_min, x_max, y_min, y_max, grid_x, grid_y
    



        