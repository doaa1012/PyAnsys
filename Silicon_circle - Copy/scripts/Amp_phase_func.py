import os
import sys
import pickle
import pandas as pd
import numpy as np
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from config import *


def Amp_phase(freq, dict_temp):
    T_wave = 1 / freq
    t_end = 5 * T_wave
    step_size = 0.25 * T_wave
    dict_keys= dict_temp.keys()
    df= pd.DataFrame()
    List=[]
    for t in np.arange(0, t_end, step_size):
        closest_key = min(dict_keys, key=lambda x: abs(x - t))
        List.append(closest_key)
    #start_index = 1
    #next_four_values = List[start_index:start_index + 4]

    middle_start = len(List) // 2 - 2 
    middle_end = middle_start + 4  
    middle_values = List[middle_start:middle_end]
    
    for x in middle_values :
        df[x]= dict_temp[x]
    
    A = ((df.iloc[:, 0] - df.iloc[:, 2])**2) + ((df.iloc[:, 1] - df.iloc[:, 3])**2)
    Amp = np.sqrt(A)
            
    phase = np.arctan((df.iloc[:, 0] - df.iloc[:, 2]) / (df.iloc[:, 1] - df.iloc[:, 3]))
            
    return Amp, phase

if __name__ == "__main__":
    node_temp_3= pd.read_pickle(Dict_temp_3)
    Amp, phase=Amp_phase(3, node_temp_3)
    print(phase)