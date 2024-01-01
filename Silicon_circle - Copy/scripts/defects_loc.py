
import numpy as np
import numpy as np
import pandas as pd

def define_defects():
    A = [
    {"x": 10e-3, "y": 10e-3, "radius": 2e-3, "depth": -5e-4},
    {"x": 70e-3, "y": 30e-3, "radius": 2e-3, "depth": -8e-3},
    {"x": 110e-3, "y": 30e-3, "radius": 4e-3, "depth": -8e-3},
    {"x": 150e-3, "y": 30e-3, "radius": 8e-3, "depth": -8e-3}]

    B = [
        {"x": 30e-3, "y": 70e-3, "radius": 6e-3, "depth": -5e-3},
        {"x": 70e-3, "y": 70e-3, "radius": 2e-3, "depth": -5e-3},
        {"x": 110e-3, "y": 70e-3, "radius": 4e-3, "depth": -5e-3},
        {"x": 150e-3, "y": 70e-3, "radius": 8e-3, "depth": -5e-3}]

    c = [
        {"x": 30e-3, "y": 110e-3, "radius": 6e-3, "depth": -7e-3},
        {"x": 70e-3, "y": 110e-3, "radius": 2e-3, "depth": -7e-3},
        {"x": 110e-3, "y":110e-3, "radius": 4e-3, "depth": -7e-3},
        {"x": 150e-3, "y": 110e-3, "radius":8e-3, "depth": -7e-3}]

    d = [
        {"x": 30e-3, "y": 150e-3, "radius": 6e-3, "depth": -6e-3},
        {"x": 70e-3, "y": 150e-3, "radius": 2e-3, "depth": -6e-3},
        {"x": 110e-3, "y":150e-3, "radius": 4e-3, "depth": -6e-3},
        {"x": 150e-3, "y": 150e-3, "radius": 8e-3, "depth": -6e-3}]

    numeric_values_A = [[item["x"], item["y"], item["radius"], item["depth"]] for item in A]
    numeric_values_B = [[item["x"], item["y"], item["radius"], item["depth"]] for item in B]
    numeric_values_c = [[item["x"], item["y"], item["radius"], item["depth"]] for item in c]
    numeric_values_d = [[item["x"], item["y"], item["radius"], item["depth"]] for item in d]
    # Combine the numeric values into a single NumPy array
    defects_loc = np.array(numeric_values_A + numeric_values_B + numeric_values_c+ numeric_values_d)
    return defects_loc