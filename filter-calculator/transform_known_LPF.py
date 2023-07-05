'''
    transform_known_LPF.py

    This file contains a method to transform a known LPF into all other types.
    This is part of filter-calculator a program to help calculate filter transformation values.

    Created:    22 June 2023
    Modified:    5 July 2023
    
'''

PI = 3.1415

def transform_known_LPF(keys_list):

    filter_values = {}

    filter_values["L_lp"] = float(input("Enter the lowpass filter inductor value in H:\t"))
    filter_values["C_lp"] = float(input("Enter the lowpass filter capacitor value in F:\t"))
    filter_values["f_0"] = float(input("Enter the cutoff frequency in Hz:\t\t"))
    filter_values["bw_Hz"] = float(input("Enter the desired bandwidth in Hz:\t\t"))

    filter_values["w_0"] = filter_values.get("f_0") * 2 * PI
    filter_values["bw_rad"] = filter_values.get("bw_Hz") * 2 * PI

    # Find the global L and C values for transformation
    L = filter_values.get("L_lp") * filter_values.get("w_0")
    C = filter_values.get("C_lp") * filter_values.get("w_0")

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