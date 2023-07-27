'''
    calculate.py

    This file acts as a library for different types of filter calculators to be used in amplifier-calculator.

    Author:     Eleanor Taylor

    Created:     26 July 2023
    Modified:    26 July 2023
    
'''

import math

PI = 3.14159
VACUUM_PERMITTIVITY = 8.8542e-12
VACUUM_PERMEABILITY = 12.566e-7
C = 3e8
ETA = VACUUM_PERMEABILITY * C

# CALCULATES POSSIBLE VALUES FOR A TUNED AMPLIFIER
def known_LPF(keys_list): # TODO: IMPLEMENT

    amplifier = {}  # Set up the return dictionary

    f_r = float(input("Enter the center frequency in Hz:\t"))
    bw = float(input("Enter the bandwidth in Hz:\t"))

    w_r = f_r * 2 * PI
    bw_rad = bw * 2 * PI

    # Set any values that didn't get set up to -1 for error checking purposes
    for key in keys_list:
        if key in amplifier:
            continue
        else:
            amplifier[key] = -1.0
    
    return amplifier