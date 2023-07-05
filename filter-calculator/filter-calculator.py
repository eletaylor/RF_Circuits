'''
    filter-calculator.py

    This is a program to help calculate filter transformation values.

    Created:    22 June 2023
    Modified:    5 July 2023
    
'''

import textwriter
import transform_known_LPF

def main():

    # List of all values tracked by this filter
    keys_list = ["f_0", "w_0", "Z_0", "bw_Hz", "bw_rad", 
                 "L_lp", "C_lp", "L_hp", "C_hp", 
                 "L_bp_series", "C_bp_series", "L_bp_parallel", "C_bp_parallel", 
                 "L_bs_parallel", "C_bs_parallel", "L_bs_series", "C_bs_series"]
    filter_values = {}

    print ("\n#######################################################################")
    print ("\nWELCOME TO FILTER CALCULATOR - Your one-stop shop for all filter needs!")
    print ("\n#######################################################################\n")

    mode = -1
    while (mode < 1):
        mode = int(input ("""\nWhich version of the calculator do you want?
                            1:  Find all transformaitons from known constant-k LPF values
                            2:  Find all constant-k transformations for a 50-ohm transmission
                                line filter of a given frequency with no known components
                            3:  Find all constant-k transformations for a non-50-ohm
                                transmission line filter with no known components"""))

        match mode:
            case 1: # TODO: Calculate Z_0 from these values
                filter_values = transform_known_LPF(keys_list)
            #case 2: # Page 735
                #L_lp = 15.9155e-9 * (1e9/f_0) 
                #C_lp = 6.3662e-12 * (1e9/f_0)
            #case 3: # Page 735 # TODO: Scale all by Z_0
                #Z_0 = float(input("Enter the characteristic impedance in Ohms:\t"))
                #L_lp = 15.9155e-9 * (1e9/f_0) 
                #C_lp = 6.3662e-12 * (1e9/f_0)
            # case 4: # Find all m-derived components with no known components, variable impedance and m-value
                #This will require some changes to be made to textwriter to accomodate more components
            case _:
                mode = -1
    
    # For a transmission line, Z_0 = sqrt(L/C)
    # If we include parasitics, Z_0 = sqrt((R + jwL)/(G + jwC))

    # w_h = 2/sqrt(LC)
    # w_0 = 1/sqrt(LC)

    # C = 1/(w_0 * Z_0)
    # L = Z_0 / w_0

    # Using an m-derived half-section like in fig. 2.9:
    #   L_1 (series) = (mL)/2
    #   L_2 (parallel, in series with C_1) = (1 - m^2)L/(2*m)
    #   C_1 (parallel, in series with L_2) = (mC)/2

    # C = (2/w_h)*(1/Z_0)
    # L = (2/w_h)*Z_0

    # Using T-sections -- the end parallel capacitors are equal to C/2
    # Using pi-sections -- the end series inductors are equal to L/2
    # In both cases, the center core sections use C and L (combining series
    # additions of L/2 + L/2)

    # If using m-derived sections:
    #   L_1 = (2m/w_1)*R
    #   L_2 = (1-m^2)*R/(2m*w_1)
    #   C_1 = (2m/w_1)*(1/Z_0)
    # Note that the T-section designs' end sections will have 2*L_2 and C_1/2

    # Table values (22.2) assume m = 0.6, so use that here.
    # m can be modified to create a notch by using m = sqrt(1 - (w_1/w_notch)^2)

    # Table 22.5 gives butterworth values, use equations 31 and 32
    # Table 22.7 gives chebyshev values
    
    # Save as a list of strings to be iterable
    '''
    text = textwriter(f_0, bw_Hz, L_lp, C_lp, L_hp, C_hp, L_bp_series, C_bp_series, L_bp_parallel, C_bp_parallel, L_bs_parallel, C_bs_parallel, L_bs_series, C_bs_series)
            
    filename = f"filters_{int(f_0)}Hz.txt"
    with open(filename, 'w+', newline= '') as textfile:
        for line in text:
            print(line)             # Print each line to the console
            textfile.write(line)    # Print each line to the text file
            textfile.write("\n")    # Add a newline character

    print(f"Transformation values saved to: {filename}")
    '''
if __name__ == "__main__":
    main()