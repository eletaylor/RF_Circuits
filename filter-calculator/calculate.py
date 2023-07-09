'''
    calculate.py

    This file acts as a library for different types of filter calculators to be used in filter-calculator.

    Author:     Eleanor Taylor

    Created:     5 July 2023
    Modified:    6 July 2023
    
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

    # Add local versions of these for ease of use
    w_0 = filter_values.get("w_0")
    bw_rad = filter_values.get("bw_rad")

    # Find the global L and C values for transformation
    L = filter_values.get("L_lp") * w_0
    C = filter_values.get("C_lp") * w_0

    # Calculate characteristic impedance
    filter_values["Z_0"] = math.sqrt(L/C)

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

# CALCULATES FILTER VALUES FOR A 50-OHM TRANSMISSION-LINE FILTER WITH CONSTANT-K SECTIONS
def constk_50ohm(keys_list):

    filter_values = {}

    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # Add local versions of these for ease of use
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

    # Scale by impedance, the original values from p 735 are for 50 Ohms
    impedance_ratio = Z / 50.0

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # Add local versions of these for ease of use
    w_0 = filter_values.get("w_0")
    bw_rad = filter_values.get("bw_rad")

    # These values are from p 735 in Planar Microwave Engineering
    filter_values["L_lp"] = 15.9155e-9 * (1e9/filter_values.get("f_0")) * impedance_ratio
    filter_values["C_lp"] = 6.3662e-12 * (1e9/filter_values.get("f_0")) / impedance_ratio
    
    # Find the global L and C values for transformation
    L = filter_values.get("L_lp") * w_0
    C = filter_values.get("C_lp") * w_0

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

# CALCULATES FILTER TRANSFORMATIONS OF A BUTTERWORTH LPF
def butterworth(keys_list):
    
    filter_values = {}  # Set up the return dictionary

    filter_values["n"] = int(input("Enter the order of the filter n:\t\t"))
    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))
    filter_values["Z_0"] = float(input("Enter the characteristic impedance in Ohms:\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # Local variables for ease of use
    n = filter_values.get("n")
    w_0 = filter_values.get("w_0")
    R = filter_values.get("Z_0")
    bw_rad = filter_values.get("bw_rad")
    b = [0] * n
    eps = 1   # Arbitrary, related to passband spec. Maybe add user config later.

    # Find the bk coefficients for the filter, each corresponds to a component.
    for k in range(1, len(b) + 1):
        b[k-1] = 2 * (pow(eps, (1.0/n))) * abs(math.sin(((2*(k+1) - 1)*PI)/(2*n)))

    # The values given are for capacitor-first design!
    # Find the LPF values for the Butterworth filter
    lpf = {}    # component name (string) : component value (float)
    for k in range(1, len(b) + 1):
        if (k % 2 == 0):
            lpf[f"L{k}"] = (R * b[k-1]) / w_0
        else:
            lpf[f"C{k}"] = b[k-1] / (w_0 * R)
    
    # Find the general values for each component to make transformation easier
    general = {}
    for component in lpf:
        general[component] = lpf[component] * w_0

    # Find the other filter values from the general LC values
    hpf = {}    # component name (string) : component value (float)
    bpf = {}    # branch name (string) : [component 1 value (float), component 2 value (float)]
    bsf = {}    # branch name (string) : [component 1 value (float), component 2 value (float)]
    for component in general:
        # Add highpass transform value
        hpf[component] = 1 / (w_0 * general[component])
        # Each componet turns into 2 for bandpass and bandstop
        bp_transform = [0,0]
        bs_transform = [0,0]
        if (component[0] == "L"): # Bandpass and bandstop transformations for an inductor
            bp_transform[0] = general[component] / bw_rad
            bp_transform[1] = bw_rad / (w_0 * w_0 * general[component])
            bpf[f"SeriesLC{component[1]}"] = bp_transform
            bs_transform[0] = (bw_rad * general[component]) / (w_0 * w_0)
            bs_transform[1] = 1 / (bw_rad * general[component])
            bsf[f"ParallelLC{component[1]}"] = bs_transform
        else: # Bandpass and bandstop transformations for a capacitor
            bp_transform[0] = bw_rad / (w_0 * w_0 * general[component])
            bp_transform[1] = general[component] / bw_rad
            bpf[f"ParallelCL{component[1]}"] = bp_transform
            bs_transform[0] = 1 / (bw_rad * general[component])
            bs_transform[1] = (bw_rad * general[component]) / (w_0 * w_0)
            bsf[f"SeriesLC{component[1]}"] = bs_transform   # TODO: double check > should this be "LC" or "CL"?

    # Add the dictionaries for each type to the dictionary of return values
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

# CALCULATES FILTER TRANSFORMATIONS OF A CHEBYSHEV LPF
def chebyshev(keys_list):
    
    filter_values = {}  # Set up the return dictionary

    n = 0
    possible_n = [3, 5, 7, 9]
    while n not in possible_n:  # Only let the user input orders that we have prototypes for in Table 22.17
        n = int(input("Enter the order of the filter n (3-9, odd only):\t"))
    filter_values["n"] = n
    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t\t"))
    filter_values["Z_0"] = float(input("Enter the characteristic impedance in Ohms:\t\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # Local variables for ease of use
    w_0 = filter_values.get("w_0")
    R = filter_values.get("Z_0")
    bw_rad = filter_values.get("bw_rad")
    # eps = 0.5   # Arbitrary, related to passband spec. Maybe add user config later. Tables 22.16-22.18 only give 0.1, 0.5, and 1
    
    # Table 22.18 for 1dB ripple
    lpf_normalized_3 = [2.024, 0.994, 2.024]
    lpf_normalized_5 = [2.135, 1.091, 3.000, 1.091, 2.135]
    lpf_normalized_7 = [2.167, 1.112, 3.094, 1.174, 3.094, 1.112, 2.167]
    lpf_normalized_9 = [2.180, 1.119, 3.121, 1.190, 3.175, 1.190, 3.121, 1.119, 2.180]

    '''
    # Table 22.17 for 0.5dB ripple
    lpf_normalized_3 = [1.596, 1.097, 1.596]
    lpf_normalized_5 = [1.706, 1.230, 2.541, 1.230, 1.706]
    lpf_normalized_7 = [1.737, 1.258, 2.638, 1.344, 2.638, 1.258, 1.737]
    lpf_normalized_9 = [1.750, 1.269, 2.668, 1.367, 2.724, 1.367, 2.668, 1.269, 1.750]
    '''

    lpf_normalized = []
    # Choose the correct normalized values for the filter order
    match n:
        case 3:
            lpf_normalized = lpf_normalized_3
        case 5:
            lpf_normalized = lpf_normalized_5
        case 7:
            lpf_normalized = lpf_normalized_7
        case 9:
            lpf_normalized = lpf_normalized_9
        case _:
            lpf_normalized = lpf_normalized_3

    # The values given are for capacitor-first design!

    lpf = {}    # component name (string) : component value (float)
    for k in range(1, n + 1):
        if (k % 2 == 0):
            lpf[f"L{k}"] = (lpf_normalized[k-1] * R) / w_0
        else:
            lpf[f"C{k}"] = (lpf_normalized[k-1] / R) / w_0
    
    # Find the general values for each component to make transformation easier
    general = {}
    for component in lpf:
        general[component] = lpf[component] * w_0

    # Find the other filter values from the general LC values
    hpf = {}    # component name (string) : component value (float)
    bpf = {}    # branch name (string) : [component 1 value (float), component 2 value (float)]
    bsf = {}    # branch name (string) : [component 1 value (float), component 2 value (float)]
    for component in general:
        # Add highpass transform value
        hpf[component] = 1 / (w_0 * general[component])
        # Each componet turns into 2 for bandpass and bandstop
        bp_transform = [0,0]
        bs_transform = [0,0]
        if (component[0] == "L"): # Bandpass and bandstop transformations for an inductor
            bp_transform[0] = general[component] / bw_rad
            bp_transform[1] = bw_rad / (w_0 * w_0 * general[component])
            bpf[f"SeriesLC{component[1]}"] = bp_transform
            bs_transform[0] = (bw_rad * general[component]) / (w_0 * w_0)
            bs_transform[1] = 1 / (bw_rad * general[component])
            bsf[f"ParallelLC{component[1]}"] = bs_transform
        else: # Bandpass and bandstop transformations for a capacitor
            bp_transform[0] = bw_rad / (w_0 * w_0 * general[component])
            bp_transform[1] = general[component] / bw_rad
            bpf[f"ParallelCL{component[1]}"] = bp_transform
            bs_transform[0] = 1 / (bw_rad * general[component])
            bs_transform[1] = (bw_rad * general[component]) / (w_0 * w_0)
            bsf[f"SeriesLC{component[1]}"] = bs_transform   # TODO: double check > should this be "LC" or "CL"?

    # Add the dictionaries for each type to the dictionary of return values
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

# CALCULATES FILTER VALUES FOR A 50-OHM TRANSMISSION-LINE FILTER WITH M-DERIVED SECTIONS
def msections_50ohm(keys_list): #TODO: IMPLEMENT

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

    filter_values = {}
    return filter_values

# CALCULATES FILTER VALUES FOR A TRANSMISSION-LINE FILTER WITH M-DERIVED SECTIONS
def msections(keys_list): #TODO: IMPLEMENT, ADD TRANSFORMATION FOR CHARACTERISTIC IMPEDANCE
    
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

    filter_values = {}
    return filter_values