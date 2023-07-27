'''
    calculate.py

    This file acts as a library for different types of filter calculators to be used in amplifier-calculator.

    Author:     Eleanor Taylor

    Created:     26 July 2023
    Modified:    26 July 2023
    
'''

import math

PI = 3.14159

#VACUUM_PERMITTIVITY = 8.8542e-12
#VACUUM_PERMEABILITY = 12.566e-7
#C = 3e8
#ETA = VACUUM_PERMEABILITY * C

# CALCULATES POSSIBLE VALUES FOR A TUNED AMPLIFIER
def tuned(keys_list):

    amplifier = {}  # Set up the return dictionary

    print("\n")

    # Prompt user for input
    f_r = float(input("Enter the center frequency in Hz:\t"))
    bw = float(input("Enter the bandwidth in Hz:\t\t"))

    # Convert to radian values
    w_r = f_r * 2 * PI
    bw_rad = bw * 2 * PI

    # Establish relationships
    quality_factor = f_r / bw
    lc_product = pow(1/(w_r), 2)
    
    # Make a list of standard inductor sizes, set up lists for corresponding components
    L = [2.2e-9, 3.3e-9, 4.7e-9, 6.8e-9, 7.5e-9, 9.1e-9, 12e-9, 16e-9, 22e-9, 27e-9, 33e-8, 43e-9, 56e-9, 68e-9,
         82e-9, 91e-9, 120e-9, 160e-9, 220e-9, 330e-9, 470e-9, 560e-9, 680e-9, 820e-9, 910e-9, 1200e-9, 2200e-9, 
         3300e-9, 4700e-9, 5600e-9, 6800e-9, 7500e-9, 8200e-9, 9100e-9]
    R = [0] * len(L)
    C = [0] * len(L)

    # Loop over the inductances to calculate values for the other components
    for i in range(len(L) - 1):
        # R = bw_rad * L
        R[i] = bw_rad * L[i]
        # C = lc_product / L
        C[i] = lc_product / L[i]

    # Add values to the dictionary
    amplifier["f_r"] = f_r
    amplifier["w_r"] = w_r
    amplifier["bw"] = bw
    amplifier["bw_rad"] = bw_rad
    amplifier["Q"] = quality_factor
    amplifier["L"] = L
    amplifier["C"] = C
    amplifier["R"] = R

    # Set any values that didn't get set up to -1 for error checking purposes
    for key in keys_list:
        if key in amplifier:
            continue
        else:
            amplifier[key] = -1.0
    
    return amplifier

# CALCULATES POSSIBLE VALUES FOR A FEEDBACK AMPLIFIER
def feedback(keys_list):    # TODO: IMPLEMENT
    amplifier = {}
    return amplifier