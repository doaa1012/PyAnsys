import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from scripts.plot_images import plot_images
import matplotlib.patches as patches


def plot_rect(loc, temp, x_near, y_near, fixed_y=0.04, fixed_x=0.07, rect_size=3, label="Temperature"):
    
    grid_temperature, x_min, x_max, y_min, y_max, grid_x, grid_y = plot_images(temp, loc, label=label, plot_image=False)
    x_index = np.argmin(np.abs(grid_x[0, :] - fixed_x))
    y_index = np.argmin(np.abs(grid_y[:, 0] - fixed_y))
    x_index_near = np.argmin(np.abs(grid_x[0, :] - x_near))
    y_index_near = np.argmin(np.abs(grid_y[:, 0] - y_near))

    # Define the size of the rectangular regions
    x_range_center = (int(x_index - rect_size), int(x_index + rect_size))
    y_range_center = (int(y_index - rect_size), int(y_index + rect_size))
    x_range_nearby = (int(x_index_near - rect_size), int(x_index_near + rect_size))
    y_range_nearby = (int(y_index_near - rect_size), int(y_index_near + rect_size))

    plt.figure(figsize=(8, 6))
    plt.imshow(grid_temperature, extent=(x_min, x_max, y_min, y_max), cmap="viridis", origin="lower", aspect="auto")
    plt.colorbar(label=label)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.scatter(grid_x[y_index, :], np.full_like(grid_x[y_index, :], fixed_y), color='red', marker='o', label='Fixed Y', s=5, alpha=0.2)

    rect_x_center = grid_x[0, x_range_center[0]]
    rect_y_center = grid_y[y_range_center[0], 0]
    rect_width_center = grid_x[0, x_range_center[1]] - rect_x_center
    rect_height_center = grid_y[y_range_center[1], 0] - rect_y_center

    rect_center = patches.Rectangle((rect_x_center, rect_y_center), rect_width_center, rect_height_center,
                                   linewidth=2, edgecolor='red', facecolor='none', label='Selected Center Region')
    plt.gca().add_patch(rect_center)

    rect_x_nearby = grid_x[0, x_range_nearby[0]]
    rect_y_nearby = grid_y[y_range_nearby[0], 0]
    rect_width_nearby = grid_x[0, x_range_nearby[1]] - rect_x_nearby
    rect_height_nearby = grid_y[y_range_nearby[1], 0] - rect_y_nearby

    rect_nearby = patches.Rectangle((rect_x_nearby, rect_y_nearby), rect_width_nearby, rect_height_nearby,
                                   linewidth=2, edgecolor='blue', facecolor='none', label='Selected Nearby Region')
    plt.gca().add_patch(rect_nearby)
  
    plt.scatter(grid_x[y_index, :], np.full_like(grid_x[y_index, :], fixed_y), color='red', marker='o', label='Fixed Y', s=5, alpha=0.2)
    plt.axis('off')
    plt.show()

