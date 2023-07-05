def constk_writer(filter_values):

    text = [
        f"\n#################################################################\n",
        f"Transformations for a filter with:",
        f"  Cutoff frequency:\t\t\t{filter_values.get('f_0')} Hz",
        f"  Characteristic impedance:\t\t{filter_values.get('Z_0')} Ohms",
        #f"  m:\t\t\t\t{filter_values.get('m')}",
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
        f"If using pi sections for the filter, the seies inductors on",
        f"  either end will have half the inductance of the core ones.",
        f"\n#################################################################\n"
        ]
    
    return text

def butterworth_writer(filter_values):

    lpf_txt = []
    for component in filter_values.get("lpf"):
        lpf_txt.append(f"{component}:\t")

    text = [
        f"\n#################################################################\n",
        f"Transformations for a filter with:",
        f"  Cutoff frequency:\t\t\t{filter_values.get('f_0')} Hz",
        f"  Characteristic impedance:\t\t{filter_values.get('Z_0')} Ohms",
        f"  Filter order:\t\t{filter_values.get('n')}",
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
        f"If using pi sections for the filter, the seies inductors on",
        f"  either end will have half the inductance of the core ones.",
        f"\n#################################################################\n"
        ]
    
    return text