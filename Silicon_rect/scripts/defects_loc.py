
import numpy as np
import numpy as np
import pandas as pd
#mapdl.block(0, sample_x, 0, sample_y, 0, sample_z)
def define_defects():
    A = [
    {"x_strat": 2e-3, "x_end": 4e-3,  "y_strat": 2e-3, "y_end": 4e-3,  "z_strat": 1.75e-3, "z_end": 2e-3 },
    {"x_strat": 70e-3, "x_end": 80e-3,  "y_strat": 70e-3, "y_end": 80e-3,  "z_strat": 4e-3, "z_end": 2e-3}]

    numeric_values_A = [[item["x_strat"], item["x_end"], item["y_strat"], item["y_end"], item["z_strat"],  item["z_end"]] for item in A]
    # Combine the numeric values into a single NumPy array
    defects_loc = np.array(numeric_values_A)

    
    return defects_loc