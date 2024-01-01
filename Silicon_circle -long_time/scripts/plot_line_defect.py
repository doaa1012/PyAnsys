import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from scripts.plot_images import plot_images


def plot_line(loc, temp, fixed_y=0.04, label="Temperature"):
    grid_temperature, x_min, x_max, y_min, y_max, grid_x, grid_y = plot_images(temp,loc,
                                                                         label= label , plot_image= False)
    y_index = np.argmin(np.abs(grid_y[:, 0] - fixed_y))
    temperature_line = grid_temperature[y_index, :]
   
    plt.figure(figsize=(8, 6))
    plt.imshow(grid_temperature, extent=(x_min, x_max, y_min, y_max), cmap="viridis", origin="lower", aspect="auto")
    plt.colorbar(label=label)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.scatter(grid_x[y_index, :], np.full_like(grid_x[y_index, :], fixed_y), color='red', marker='o', label='Fixed Y', s=5, alpha=0.2)
    plt.axis('off')
    plt.show()

    # Plot the line response
    plt.figure(figsize=(6, 5))
    plt.plot(grid_x[y_index, :], temperature_line)
    plt.xlabel("X-coordinate")
    plt.ylabel("Temperature")
    plt.title(f"Temperature Line Response at y = {fixed_y}")
    plt.grid(True)
    plt.show()