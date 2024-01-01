import os
import sys
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from scripts.plot_images import plot_images

def compute_amplitude_phase(temps):
    # Zero-padding for improved frequency resolution
    n = len(temps)
    temps_padded = np.pad(temps, (0, n), 'constant')

    # Calculate the FFT of the temps data with zero-padding
    sp = np.fft.fft(temps_padded)
    frequencies = np.fft.fftfreq(len(temps_padded))

    # Find the peaks in the FFT spectrum
    peaks, _ = find_peaks(np.abs(sp))  # Adjust height threshold as needed

    if len(peaks) == 0:
        return 0.0, 0.0  # No peaks found, return zero amplitude and phase

    # Get the index of the highest peak (ignoring DC component at index 0)
    peak_index = peaks[0]

    # Calculate amplitude and phase
    amplitude = np.abs(sp[peak_index]) / len(temps_padded) * 2
    phase = np.angle(sp[peak_index])
    phase_deg = np.degrees(phase)  # Convert phase from radians to degrees

    phase_deg = np.unwrap([phase_deg])[0]
    return amplitude, phase_deg



def read_func(all_node_temperatures,all_node_locations):
    all_frames = []
    for frame_key in all_node_temperatures:
        temps = all_node_temperatures[frame_key]
        grid_temperature, _, _, _, _, _, _ = plot_images(temps, all_node_locations, plot_image=False)
        grid_temperature = np.flipud(grid_temperature)
        #grid_temperature = np.fliplr(grid_temperature)
        
        all_frames.append(grid_temperature)
  
    # Now, let's compute amplitude and phase for each pixel across all frames
    height, width = all_frames[0].shape
    amplitude_img = np.zeros((height, width))
    phase_img = np.zeros((height, width))

    for x in range(height):
        for y in range(width):
            temps = [frame[x, y] for frame in all_frames]
            amplitude, phase = compute_amplitude_phase(temps)
            amplitude_img[x, y] = amplitude
            phase_img[x, y] = phase

        # Plotting Amplitude Image
    plt.figure(figsize=(10, 6))
    plt.imshow(amplitude_img, cmap='jet',  origin='upper')
    #plt.title('Amplitude Image')
    plt.colorbar(label='Amplitude')
    plt.axis('off')
   
    plt.show()

    # Plotting Phase Image
    plt.figure(figsize=(10, 6))
    plt.imshow(phase_img, cmap='jet', origin='upper')
    plt.colorbar(label='Phase')
    plt.axis('off')
    plt.show()
