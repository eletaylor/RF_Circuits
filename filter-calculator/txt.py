'''
    txt.py

    This file acts as a library of text functions for different types of filters to
    display their output in a user-friendly manner.
    
    Author:     Eleanor Taylor

    Created:     5 July 2023
    Modified:    10 July 2023
    
'''

def constk_writer(filter_values):

    text = [
        f"\n#################################################################\n",
        f"Transformations for a filter with:",
        f"  Cutoff frequency:\t\t\t{filter_values.get('f_0')} Hz",
        f"  Characteristic impedance:\t\t{filter_values.get('Z_0')} Ohms",
        f"\n######################### LOWPASS FILTER ########################\n",
        f"Inductor (L_lp):\t\t\t{filter_values.get('L_lp')} H",
        f"Capacitor (C_lp):\t\t\t{filter_values.get('C_lp')} F",
        f"\n######################## HIGHPASS FILTER ########################\n",
        f"Inductor (L_hp):\t\t\t{filter_values.get('L_hp')} H",
        f"Capacitor (C_hp):\t\t\t{filter_values.get('C_hp')} F",
        f"\n######################## BANDPASS FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{filter_values.get('bw_Hz')} Hz",
        f"Series inductor (L_bp_series):\t\t{filter_values.get('L_bp_series')} H",
        f"Series capacitor (C_bp_series):\t\t{filter_values.get('C_bp_series')} F",
        f"Parallel inductor (L_bp_parallel):\t{filter_values.get('L_bp_parallel')} H",
        f"Parallel capacitor (C_bp_parallel):\t{filter_values.get('C_bp_parallel')} F",
        f"\n######################## BANDSTOP FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{filter_values.get('bw_Hz')} Hz",
        f"Parallel inductor (L_bs_parallel):\t{filter_values.get('L_bs_parallel')} H",
        f"Parallel capacitor (C_bs_parallel):\t{filter_values.get('C_bs_parallel')} F",
        f"Series inductor (L_bs_series):\t\t{filter_values.get('L_bs_series')} H",
        f"Series capacitor (C_bs_series):\t\t{filter_values.get('C_bs_series')} F",
        f"\n#################################################################\n",
        f"This calculator gives values for \"core\" components.",
        f"If using T sections for the filter, the parallel capacitors on",
        f"  either end will have half the capacitance of the core ones.",
        f"If using pi sections for the filter, the series inductors on",
        f"  either end will have half the inductance of the core ones.",
        f"\n#################################################################\n"
        ]
    
    return text

def butterworth_writer(filter_values):

    lpf_txt = ""
    for component in filter_values.get("LPF"):
        lpf_txt += (f"{component}:\t{filter_values.get('LPF').get(component)}\n")
    hpf_txt = ""
    for component in filter_values.get("HPF"):
        hpf_txt += (f"{component}:\t{filter_values.get('HPF').get(component)}\n")
    bpf_txt = ""
    for component in filter_values.get("BPF"):
        bpf_txt += (f"{component}:\t{filter_values.get('BPF').get(component)[0]}, {filter_values.get('BPF').get(component)[1]}\n")
    bsf_txt = ""
    for component in filter_values.get("BSF"):
        bsf_txt += (f"{component}:\t{filter_values.get('BSF').get(component)[0]}, {filter_values.get('BSF').get(component)[1]}\n")

    text = [
        f"\n#################################################################\n",
        f"Transformations for a Butterworth filter with:",
        f"  Cutoff frequency:\t\t\t{filter_values.get('f_0')} Hz",
        f"  Characteristic impedance:\t\t{filter_values.get('Z_0')} Ohms",
        f"  Filter order:\t\t\t\t{filter_values.get('n')}",
        f"\n######################### LOWPASS FILTER ########################\n",
        f"{lpf_txt}",
        f"######################## HIGHPASS FILTER ########################\n",
        f"{hpf_txt}",
        f"######################## BANDPASS FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{filter_values.get('bw_Hz')} Hz",
        f"{bpf_txt}",
        f"######################## BANDSTOP FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{filter_values.get('bw_Hz')} Hz",
        f"{bsf_txt}",
        f"#################################################################\n",
        f"This calculator assumed capacitor-first design. With an even",
        f"filter order, the values will all be the same, but backwards.",
        f"With an odd filter order, the values should be symmetrical.",
        f"\n#################################################################\n"
        ]
    
    return text

def chebyshev_writer(filter_values):
    
    lpf_txt = ""
    for component in filter_values.get("LPF"):
        lpf_txt += (f"{component}:\t{filter_values.get('LPF').get(component)}\n")
    hpf_txt = ""
    for component in filter_values.get("HPF"):
        hpf_txt += (f"{component}:\t{filter_values.get('HPF').get(component)}\n")
    bpf_txt = ""
    for component in filter_values.get("BPF"):
        bpf_txt += (f"{component}:\t{filter_values.get('BPF').get(component)[0]}, {filter_values.get('BPF').get(component)[1]}\n")
    bsf_txt = ""
    for component in filter_values.get("BSF"):
        bsf_txt += (f"{component}:\t{filter_values.get('BSF').get(component)[0]}, {filter_values.get('BSF').get(component)[1]}\n")

    text = [
        f"\n#################################################################\n",
        f"Transformations for a Chebyshev filter with:",
        f"  Cutoff frequency:\t\t\t{filter_values.get('f_0')} Hz",
        f"  Characteristic impedance:\t\t{filter_values.get('Z_0')} Ohms",
        f"  Filter order:\t\t\t\t{filter_values.get('n')}",
        f"\n######################### LOWPASS FILTER ########################\n",
        f"{lpf_txt}",
        f"######################## HIGHPASS FILTER ########################\n",
        f"{hpf_txt}",
        f"######################## BANDPASS FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{filter_values.get('bw_Hz')} Hz",
        f"{bpf_txt}"
        f"\n######################## BANDSTOP FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{filter_values.get('bw_Hz')} Hz",
        f"{bsf_txt}",
        f"#################################################################\n",
        f"This calculator assumed capacitor-first design and a ripple of\n" 
        f"1 dB in the passband.\n"
        f"\n#################################################################\n"
        ]
    
    return text

def microstrip_writer(filter_values):

    text = [
        f"\n#################################################################\n",
        f"Component lengths for a microstrip LPF with",
        f"  Cutoff frequency:\t\t\t{filter_values.get('f_0')} Hz",
        f"  Characteristic impedance:\t\t{filter_values.get('Z_0')} Ohms",
        f"  Relative permittivity:\t\t{filter_values.get('relative_permittivity')}",
        f"\n################# EQUIVALENT LUMPED CIRCUIT #####################\n",
        f"Inductor (L_lp):\t\t\t{filter_values.get('lumped_L_lp')} H",
        f"Capacitor (C_lp):\t\t\t{filter_values.get('lumped_C_lp')} F",
        f"\n############################ LENGTHS ############################\n",
        f"Normalized inductor length (l_L_deg):\t{filter_values.get('l_L_deg')} deg",
        f"Normalized capacitor length (l_C_deg):\t{filter_values.get('l_C_deg')} deg",
        f"Physical inductor length (l_L):\t\t{filter_values.get('l_L')} mm",
        f"Physical capacitor length (l_C):\t{filter_values.get('l_C')} mm",
        f"\n#################################################################\n",
        f"This calculator gives values for \"core\" components.",
        f"If using T sections for the filter, the capacitors on either end",
        f"  will have half the length of the core ones.",
        f"If using pi sections for the filter, the inductors on either end",
        f"  will have half the length of the core ones.",
        f"Each microstrip filter should have 7 components: 2 half end",
        f"  sections and 5 \"core\" sections.",
        f"Width is not given. Simply go as wide as possible for capacitors",
        f"  and as thin as possible for inductors.",
        f"\n#################################################################\n"
        ]
    
    return text