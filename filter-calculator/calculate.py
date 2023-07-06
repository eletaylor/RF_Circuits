'''
    calculate.py

    This file acts as a library for different types of filter calculators to be used in filter-calculator.

    Created:     5 July 2023
    Modified:    5 July 2023
    
'''

import math
PI = 3.1415

# CALCULATES FILTER TRANSFORMATIONS FROM A KNOWN LOW-PASS FILTER USING CONSTANT-K SECTIONS
def known_LPF(keys_list):

    filter_values = {}  # Set up the return dictionary

    filter_values["L_lp"] = float(input("Enter the lowpass filter inductor value in H:\t"))
    filter_values["C_lp"] = float(input("Enter the lowpass filter capacitor value in F:\t"))
    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # Find the global L and C values for transformation
    L = filter_values.get("L_lp") * filter_values.get("w_0")
    C = filter_values.get("C_lp") * filter_values.get("w_0")

    # Calculate characteristic impedance
    filter_values["Z_0"] = math.sqrt(L/C)

    # Find the highpass filter values from the global LC
    filter_values["L_hp"] = 1/(filter_values.get("w_0") * L)
    filter_values["C_hp"] = 1/(filter_values.get("w_0") * C)

    # Find the bandpass filter values from the global LC
    filter_values["L_bp_series"] = L/filter_values.get("bw_rad")
    filter_values["C_bp_series"] = filter_values.get("bw_rad")/(filter_values.get("w_0") * filter_values.get("w_0") * L)
    filter_values["L_bp_parallel"] = filter_values.get("bw_rad")/(filter_values.get("w_0") * filter_values.get("w_0") * C)
    filter_values["C_bp_parallel"] = C/filter_values.get("bw_rad")

    # Find the bandstop filter values from the global LC
    filter_values["L_bs_parallel"] = (filter_values.get("bw_rad") * L) / (filter_values.get("w_0") * filter_values.get("w_0"))
    filter_values["C_bs_parallel"] = 1/(filter_values.get("bw_rad") * L)
    filter_values["L_bs_series"] = 1/(filter_values.get("bw_rad") * C)
    filter_values["C_bs_series"] = (filter_values.get("bw_rad") * C) / (filter_values.get("w_0") * filter_values.get("w_0"))

    # Set any values that didn't get set up to -1 for error checking purposes
    for key in keys_list:
        if key in filter_values:
            continue
        else:
            filter_values[key] = -1.0
    
    return filter_values

# CALCULATES FILTER VALUES FOR A 50-OHM TRANSMISSION-LINE FILTER WITH CONSTANT-K SECTIONS
def constk_50ohm(keys_list):

    filter_values = {}

    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    w_0 = filter_values.get("w_0")
    bw_rad = filter_values.get("bw_rad")

    # These values are from p 735 in Planar Microwave Engineering
    filter_values["L_lp"] = 15.9155e-9 * (1e9/filter_values.get("f_0")) 
    filter_values["C_lp"] = 6.3662e-12 * (1e9/filter_values.get("f_0"))
    
    # Find the global L and C values for transformation
    L = filter_values.get("L_lp") * w_0
    C = filter_values.get("C_lp") * w_0

    # Calculate characteristic impedance
    filter_values["Z_0"] = math.sqrt(L/C) # If we include parasitics, Z_0 = sqrt((R + jwL)/(G + jwC))

    # Find the highpass filter values from the global LC
    filter_values["L_hp"] = 1/(w_0 * L)
    filter_values["C_hp"] = 1/(w_0 * C)

    # Find the bandpass filter values from the global LC
    filter_values["L_bp_series"] = L/bw_rad
    filter_values["C_bp_series"] = bw_rad/(w_0 * w_0 * L)
    filter_values["L_bp_parallel"] = bw_rad/(w_0 * w_0 * C)
    filter_values["C_bp_parallel"] = C/bw_rad

    # Find the bandstop filter values from the global LC
    filter_values["L_bs_parallel"] = (bw_rad * L) / (w_0 * w_0)
    filter_values["C_bs_parallel"] = 1/(bw_rad * L)
    filter_values["L_bs_series"] = 1/(bw_rad * C)
    filter_values["C_bs_series"] = (bw_rad * C) / (w_0 * w_0)

    # Set any values that didn't get set up to -1 for error checking purposes
    for key in keys_list:
        if key in filter_values:
            continue
        else:
            filter_values[key] = -1.0
    
    return filter_values

# CALCULATES FILTER VALUES FOR A TRANSMISSION-LINE FILTER WITH CONSTANT-K SECTIONS
def constk(keys_list):

    filter_values = {}

    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))
    Z = float(input("Enter the characteristic impedance in Ohms:\t"))

    impedance_ratio = Z / 50.0

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # These values are from p 735 in Planar Microwave Engineering
    filter_values["L_lp"] = 15.9155e-9 * (1e9/filter_values.get("f_0")) * impedance_ratio
    filter_values["C_lp"] = 6.3662e-12 * (1e9/filter_values.get("f_0")) / impedance_ratio
    
    # Find the global L and C values for transformation
    L = filter_values.get("L_lp") * filter_values.get("w_0")
    C = filter_values.get("C_lp") * filter_values.get("w_0")

    filter_values["Z_0"] = math.sqrt(L/C) # If we include parasitics, Z_0 = sqrt((R + jwL)/(G + jwC))

    # Find the highpass filter values from the global LC
    filter_values["L_hp"] = 1/(filter_values.get("w_0") * L)
    filter_values["C_hp"] = 1/(filter_values.get("w_0") * C)

    # Find the bandpass filter values from the global LC
    filter_values["L_bp_series"] = L/filter_values.get("bw_rad")
    filter_values["C_bp_series"] = filter_values.get("bw_rad")/(filter_values.get("w_0") * filter_values.get("w_0") * L)
    filter_values["L_bp_parallel"] = filter_values.get("bw_rad")/(filter_values.get("w_0") * filter_values.get("w_0") * C)
    filter_values["C_bp_parallel"] = C/filter_values.get("bw_rad")

    # Find the bandstop filter values from the global LC
    filter_values["L_bs_parallel"] = (filter_values.get("bw_rad") * L) / (filter_values.get("w_0") * filter_values.get("w_0"))
    filter_values["C_bs_parallel"] = 1/(filter_values.get("bw_rad") * L)
    filter_values["L_bs_series"] = 1/(filter_values.get("bw_rad") * C)
    filter_values["C_bs_series"] = (filter_values.get("bw_rad") * C) / (filter_values.get("w_0") * filter_values.get("w_0"))

    # Set any values that didn't get set up to -1 for error checking purposes
    for key in keys_list:
        if key in filter_values:
            continue
        else:
            filter_values[key] = -1.0
    
    return filter_values

# CALCULATES FILTER TRANSFORMATIONS OF A BUTTERWORTH LPF
def butterworth(keys_list):
    
    filter_values = {}  # Set up the return dictionary

    filter_values["n"] = int(input("Enter the order of the filter n:\t\t"))
    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))
    filter_values["Z_0"] = float(input("Enter the characteristic impedance in Ohms:\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    eps = 0.5   # Arbitrary, related to passband spec. Maybe add user config later.
    n = filter_values.get("n")
    b = [0] * n
    w_0 = filter_values.get("w_0")
    R = filter_values.get("Z_0")
    bw_rad = filter_values.get("bw_rad")

    for k in range(1, len(b) + 1):
        b[k-1] = 2 * (pow(eps, (1.0/n))) * abs(math.sin(((2*(k+1) - 1)*PI)/(2*n)))

    # The values given are for capacitor-first design!
    # Find the LPF values for the Butterworth filter
    lpf = {}
    for k in range(1, len(b) + 1):
        if (k % 2 == 0):
            lpf[f"L{k}"] = (R * b[k-1]) / w_0
        else:
            lpf[f"C{k}"] = b[k-1] / (w_0 * R)
    
    # Find the general values for each component to make transformation easier
    general = {}
    for component in lpf:
        general[component] = lpf[component] * w_0

    # Find the other filter values from the global LC
    hpf = {}
    bpf = {}
    bsf = {}
    for component in general:
        hpf[component] = 1 / (w_0 * general[component])
        bp_transform = [0,0]
        bs_transform = [0,0]
        if (component[0] == "L"):
            bp_transform[0] = general[component] / bw_rad
            bp_transform[1] = bw_rad / (w_0 * w_0 * general[component])
            bpf[f"SeriesLC{component[1]}"] = bp_transform
            bs_transform[0] = (bw_rad * general[component]) / (w_0 * w_0)
            bs_transform[1] = 1 / (bw_rad * general[component])
            bsf[f"ParallelLC{component[1]}"] = bs_transform
        else:
            bp_transform[0] = bw_rad / (w_0 * w_0 * general[component])
            bp_transform[1] = general[component] / bw_rad
            bpf[f"ParallelCL{component[1]}"] = bp_transform
            bs_transform[0] = 1 / (bw_rad * general[component])
            bs_transform[1] = (bw_rad * general[component]) / (w_0 * w_0)
            bsf[f"SeriesLC{component[1]}"] = bs_transform

    filter_values["LPF"] = lpf
    filter_values["HPF"] = hpf
    filter_values["BPF"] = bpf
    filter_values["BSF"] = bsf

    # Set any values that didn't get set up to -1 for error checking purposes
    for key in keys_list:
        if key in filter_values:
            continue
        else:
            filter_values[key] = -1.0
    
    return filter_values

# If using m-derived sections:
#   L_1 = (2m/w_1)*R
#   L_2 = (1-m^2)*R/(2m*w_1)
#   C_1 = (2m/w_1)*(1/Z_0)
# Note that the T-section designs' end sections will have 2*L_2 and C_1/2

    # Using an m-derived half-section like in fig. 2.9: 
    #   L_1 (series) = (mL)/2
    #   L_2 (parallel, in series with C_1) = (1 - m^2)L/(2*m)
    #   C_1 (parallel, in series with L_2) = (mC)/2

# Table values (22.2) assume m = 0.6, so use that here.
# m can be modified to create a notch by using m = sqrt(1 - (w_1/w_notch)^2)

# CALCULATES FILTER VALUES FOR A 50-OHM TRANSMISSION-LINE FILTER WITH M-DERIVED SECTIONS
def msections_50ohm(keys_list): #TODO: IMPLEMENT
    filter_values = {}
    return filter_values

# CALCULATES FILTER VALUES FOR A TRANSMISSION-LINE FILTER WITH M-DERIVED SECTIONS
def msections_50ohm(keys_list): #TODO: IMPLEMENT, ADD TRANSFORMATION FOR CHARACTERISTIC IMPEDANCE
    filter_values = {}
    return filter_values