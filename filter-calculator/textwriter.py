def textwriter(
    f_0,
    L_lp, C_lp, 
    L_hp, C_hp, 
    L_bp_series, C_bp_series, L_bp_parallel, C_bp_parallel,
    L_bs_parallel, C_bs_parallel, L_bs_series, C_bs_series):

    return [
        f"\n#################################################################\n",
        f"Transformations for a filter with cutoff frequency {f_0} Hz",
        f"\n######################### LOWPASS FILTER ########################\n",
        f"Inductor (L_lp):\t\t\t{L_lp} H",
        f"Capacitor (C_lp):\t\t\t{C_lp} F",
        f"\n######################## HIGHPASS FILTER ########################\n",
        f"Inductor (L_hp):\t\t\t{L_hp} H",
        f"Capacitor (C_hp):\t\t\t{C_hp} F",
        f"\n######################## BANDPASS FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{bw_Hz} Hz",
        f"Series inductor (L_bp_series):\t\t{L_bp_series} H",
        f"Series capacitor (C_bp_series):\t\t{C_bp_series} F",
        f"Parallel inductor (L_bp_parallel):\t{L_bp_parallel} H",
        f"Parallel capacitor (C_bp_parallel):\t{C_bp_parallel} F",
        f"\n######################## BANDSTOP FILTER ########################\n",
        f"Bandwidth (bw_Hz):\t\t\t{bw_Hz} Hz",
        f"Parallel inductor (L_bs_parallel):\t{L_bs_parallel} H",
        f"Parallel capacitor (C_bs_parallel):\t{C_bs_parallel} F",
        f"Series inductor (L_bs_series):\t\t{L_bs_series} H",
        f"Series capacitor (C_bs_series):\t\t{C_bs_series} F",
        f"\n#################################################################\n"
        ]
