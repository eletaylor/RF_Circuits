'''
    filter-calculator.py

    This is a program to help calculate filter transformation values.

    Created:    22 June 2023
    Modified:    4 July 2023
    
'''

PI = 3.1415

def main():

    print ("\n#################################################################\n")

    L_lp = float(input("Enter the lowpass filter inductor value in H:\t"))
    C_lp = float(input("Enter the highpass filter capacitor value in F:\t"))

    f_0 = float(input("Enter the cutoff frequency in Hz:\t"))
    bw_Hz = float(input("Enter the desired bandwidth in Hz:\t"))
    
    # For a transmission line, Z_0 = sqrt(L/C)
    # If we include parasitics, Z_0 = sqrt((R + jwL)/(G + jwC))

    w_0 = f_0 * 2 * PI
    bw_rad = bw_Hz * 2 * PI

    # Find the global L and C values for transformation
    L = L_lp * w_0
    C = C_lp * w_0

    # Find the highpass filter values from the global LC
    L_hp = 1/(w_0 * L)
    C_hp = 1/(w_0 * C)

    # Find the bandpass filter values from the global LC
    L_bp_series = L/bw_rad
    C_bp_series = bw_rad/(w_0 * w_0 * L)
    L_bp_parallel = bw_rad/(w_0 * w_0 * C)
    C_bp_parallel = C/bw_rad

    # Find the bandstop filter values from the global LC
    L_bs_parallel = (bw_rad * L) / (w_0 * w_0)
    C_bs_parallel = 1/(bw_rad * L)
    L_bs_series = 1/(bw_rad * C)
    C_bs_series = (bw_rad * C) / (w_0 * w_0)
    
    # Save as a list of strings to be iterable
    text = [
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
            
    filename = f"filters_{int(f_0)}Hz.txt"
    with open(filename, 'w+', newline= '') as textfile:
        for line in text:
            print(line)             # Print each line to the console
            textfile.write(line)    # Print each line to the text file
            textfile.write("\n")    # Add a newline character

    print(f"Transformation values saved to: {filename}")

if __name__ == "__main__":
    main()