import os
import json
import pandas as pd


this_dir = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(this_dir, "data")
SCRIPT_DIR = os.path.join(this_dir, "scripts")
Roll_Mapping= os.path.join(this_dir,"roll_mapping.p")
# Folder data paths
DATA_RAW_PATH = os.path.join(DATA_DIR, "raw")
DATA_CLEAN_PATH = os.path.join(DATA_DIR, "clean")

# Clean data
DATA_CLEAN_Temp = os.path.join(DATA_CLEAN_PATH, "Temperature")
Dict_temp_1 = os.path.join(DATA_CLEAN_Temp, "dict_temp_1.p")
Dict_temp_1_5 = os.path.join(DATA_CLEAN_Temp, "dict_temp_1_5.p")
Dict_temp_2 = os.path.join(DATA_CLEAN_Temp, "dict_temp_2.p")
Dict_temp_2_5 = os.path.join(DATA_CLEAN_Temp, "dict_temp_2_5.p")
Dict_temp_3 = os.path.join(DATA_CLEAN_Temp, "dict_temp_3.p")
Dict_temp_3_5 = os.path.join(DATA_CLEAN_Temp, "dict_temp_3_5.p")
Dict_temp_4 = os.path.join(DATA_CLEAN_Temp, "dict_temp_4.p")
Dict_temp_2_without_defects = os.path.join(DATA_CLEAN_Temp, "dict_temp_2_without_defects.p")

Data_to_amp= os.path.join(DATA_CLEAN_PATH,"data_to_amp")




DATA_CLEAN_Loc = os.path.join(DATA_CLEAN_PATH, "Location")
Nodes_loc_1 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_1.p")
Nodes_loc_1_5 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_1_5.p")
Nodes_loc_2 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_2.p")
Nodes_loc_2_5 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_2_5.p")
Nodes_loc_2_without_defects = os.path.join(DATA_CLEAN_Loc, "nodes_loc_2_without_defects.p")
Nodes_loc_3 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_3.p")
Nodes_loc_3_5 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_3_5.p")
Nodes_loc_4 = os.path.join(DATA_CLEAN_Loc, "nodes_loc_4.p")



DATA_CLEAN_Larger_Density = os.path.join(DATA_CLEAN_PATH, "Larger_density")

Larger_Density_Temp = os.path.join(DATA_CLEAN_Larger_Density, "Temperature")
Large_Dict_temp_1_5 = os.path.join(Larger_Density_Temp, "dict_temp_1_5.p")

Larger_Density_Loc = os.path.join(DATA_CLEAN_Larger_Density, "Location")
Larger_Density_loc_1_5 = os.path.join(Larger_Density_Loc, "nodes_loc_1_5.p")

Larger_Density_amp = os.path.join(DATA_CLEAN_Larger_Density, "large_density_amp")



