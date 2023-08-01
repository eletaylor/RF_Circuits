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
    gain_dB = float(input("Enter the gain in dB:\t\t\t"))

    # Convert values for various calculations
    w_r = f_r * 2 * PI
    bw_rad = bw * 2 * PI
    gain_V = pow(10, gain_dB / 20)

    # Establish relationships
    quality_factor = f_r / bw
    lc_product = pow(1/(w_r), 2)
    
    # Make a list of standard resistor sizes, set up lists for corresponding components
    RC = [470, 520, 640, 750, 830, 910, 1000, 1200, 1400, 1600, 1800, 2200]
    L = [0] * len(RC)
    RE = [0] * len(L)
    C = [0] * len(L)

    # Loop over the resistances to calculate values for the other components
    for i in range(len(RC)):
        C[i] = 1/(RC[i] * bw_rad)
        L[i] = lc_product / C[i]
        RE[i] = 1/(C[i] * gain_V * bw_rad)

    # Add values to the dictionary
    amplifier["f_r"] = f_r
    amplifier["w_r"] = w_r
    amplifier["bw"] = bw
    amplifier["bw_rad"] = bw_rad
    amplifier["Q"] = quality_factor
    amplifier["gain_dB"] = gain_dB
    amplifier["L"] = L
    amplifier["C"] = C
    amplifier["R_E"] = RE
    amplifier["R_C"] = RC

    # Set any values that didn't get set up error checking purposes
    for key in keys_list:
        if key in amplifier:
            continue
        else:
            amplifier[key] = "ERROR"
    
    return amplifier

# CALCULATES POSSIBLE VALUES FOR A FEEDBACK AMPLIFIER
def feedback(keys_list):    # TODO: IMPLEMENT

    amplifier = {}

    print("\n")

    # Prompt user for input
    f_0 = float(input("Enter the center frequency in Hz:\t"))
    gain_dB = float(input("Enter the gain of the amplifier in dB:\t"))
    Vdd = float(input("Enter the supply voltage in V:\t"))

    #R_L > need a load and source impedance
    



    return amplifier