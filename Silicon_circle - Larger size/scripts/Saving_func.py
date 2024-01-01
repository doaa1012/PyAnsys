import numpy as np
import pandas as pd
import pickle
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from scripts.Amp_phase_func import *
from scripts.plot_images import plot_images
from config import *
from scripts.SNR import *
from scripts.get_freq_mu import *
from scripts.get_depth import *

def save_amp_phase(freq, DATA_CLEAN_Temp, output_path):
    # For calculating the  amplitude and phase
    i=0
    Result=pd.DataFrame()
    for filename in os.listdir(DATA_CLEAN_Temp):
        Dict = os.path.join(DATA_CLEAN_Temp, filename)
        node_temp= pd.read_pickle(Dict)
        Result["Amplitude"],Result["Phase"] =Amp_phase(freq[i], node_temp)
        csv_file_path = os.path.join(output_path, f'df_{freq[i]}.csv')
        
        Result.to_csv(csv_file_path, index=False)
        i= i+1


def plotting_all(loc,path):
    nodes_loc=pd.read_pickle(loc)
    for file in os.listdir(path):
        print(file)
        df_path= os.path.join(path, file)
        df_res= pd.read_csv(df_path)
        grid_temperature, x_min, x_max, y_min, y_max, grid_x, grid_y= plot_images(df_res["Amplitude"], nodes_loc, label="Amplitude", plot_image=True)
        grid_temperature, x_min, x_max, y_min, y_max, grid_x, grid_y= plot_images(df_res["Phase"], nodes_loc, label="Phase", plot_image=True)


def get_df_CNR_phase(Data_to_amp,loaded_nodes_loc,fixed_y=0.012, fixed_x=0.012, rect_size=5, margin=6):
    df_SNR = pd.DataFrame(columns=["Frequency", "SNR", "phase_difference"]) 
    csv_files = [file for file in os.listdir(Data_to_amp) if file.endswith('.csv')]
    for csv_file in csv_files:
        frequency_str = csv_file.split('_')[1].replace('.csv', '')
        freq = float(frequency_str)  
        print("For frequency:",freq)
        df_path = os.path.join(Data_to_amp, csv_file)
        df_res = pd.read_csv(df_path)
        snr_values, phase_diff_values = SNR(loaded_nodes_loc, df_res.Phase, fixed_y=fixed_y, fixed_x=fixed_x, rect_size=rect_size, margin=margin, label="Phase")
        df_SNR = df_SNR.append({"Frequency":freq,"SNR": snr_values, "phase_difference": abs(phase_diff_values)}, ignore_index=True)
    return df_SNR

def get_df_CNR_Amp(Data_to_amp,loaded_nodes_loc, fixed_y=0.012, fixed_x=0.012, rect_size=5, margin=6):
    df_SNR_Amp = pd.DataFrame(columns=["Frequency", "SNR", "phase_difference"])  
    csv_files = [file for file in os.listdir(Data_to_amp) if file.endswith('.csv')]
    for csv_file in csv_files:
        # Extract frequency from the file name
        frequency_str = csv_file.split('_')[1].replace('.csv', '')
        freq = float(frequency_str)  # Convert the frequency string to a float
        df_path = os.path.join(Data_to_amp, csv_file)
        df_res = pd.read_csv(df_path)
        snr_values, phase_diff_values = SNR(loaded_nodes_loc, df_res.Amplitude, fixed_y=fixed_y, fixed_x=fixed_x, rect_size=rect_size, margin=margin, label="Amplitude")
        df_SNR_Amp = df_SNR_Amp.append({"Frequency":freq,"SNR": snr_values, "phase_difference": abs(phase_diff_values)}, ignore_index=True)
    return df_SNR_Amp

def depth_of_all(loc, Data_to_amp):
    df_phase_depth = pd.DataFrame(columns=["Frequency","phase_difference", "Depth"])  # Create an empty DataFrame
    csv_files = [file for file in os.listdir(Data_to_amp) if file.endswith('.csv')]

    # Process each CSV file
    for csv_file in csv_files:
        # Extract frequency from the file name
        frequency_str = csv_file.split('_')[1].replace('.csv', '')
        freq = float(frequency_str)  # Convert the frequency string to a float
        
        # Read the CSV file using pandas
        csv_path = os.path.join(Data_to_amp, csv_file)
        df = pd.read_csv(csv_path)
        phase_diff_values, depth =get_depth(freq, loc, df.Phase , fixed_y=0.01, fixed_x=0.01, rect_size=3, margin=1, label="Temperature")
        df_phase_depth = df_phase_depth.append({"Frequency":freq, "Depth": depth*1000, "phase_difference": abs(phase_diff_values)}, ignore_index=True)
    return df_phase_depth