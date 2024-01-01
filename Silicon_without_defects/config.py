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

DATA_CLEAN_Temp_without = os.path.join(DATA_CLEAN_PATH, "Temperature_without")
Dict_temp_1_without = os.path.join(DATA_CLEAN_Temp_without, "dict_temp_1.p")


DATA_CLEAN_Loc_without = os.path.join(DATA_CLEAN_PATH, "Location_without")
Nodes_loc_1_without = os.path.join(DATA_CLEAN_Loc_without, "nodes_loc_1.p")








