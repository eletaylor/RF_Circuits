'''
    filter-calculator.py

    This is a program to help calculate filter transformation values.

    Created:    22 June 2023
    Modified:    5 July 2023
    
'''

import txt
import calculate

def main():

    # List of all values tracked by the constant-k section calculators
    constk_keys_list = ["f_0", "w_0", "Z_0", "bw_Hz", "bw_rad",
                 "L_lp", "C_lp", "L_hp", "C_hp", 
                 "L_bp_series", "C_bp_series", "L_bp_parallel", "C_bp_parallel", 
                 "L_bs_parallel", "C_bs_parallel", "L_bs_series", "C_bs_series"]
    filter_values = {}

    print ("\n#######################################################################")
    print ("\nWELCOME TO FILTER CALCULATOR - Your one-stop shop for all filter needs!")
    print ("\n#######################################################################\n")

    mode = 0
    while (mode < 1):
        print ("""\nWhich version of the calculator do you want?
        1:  Find all transformaitons from known constant-k LPF values
        2:  Find all transformations for a 50-ohm constant-k transmission line
        3:  Find all transformations for any constant-k transmission line
        4:  Find all transformations for a Butterworth filter\n""")
        mode = int(input())

        match mode:
            case 1:
                filter_values = calculate.known_LPF(constk_keys_list)
                text = txt.constk_writer(filter_values)
            case 2:
                filter_values = calculate.constk_50ohm(constk_keys_list)
                text = txt.constk_writer(filter_values)
            case 3:
                filter_values = calculate.constk(constk_keys_list)
                text = txt.constk_writer(filter_values)
            case 4:
                filter_values = calculate.butterworth()
                text = txt.butterworth_writer(filter_values)
            # case x: # Find all m-derived components with a variable m-value
                #This will require a new textwriter method
            # case x: # Find all m-derived components with a variable m-value and characteristic impedance
                #This will require a new textwriter method
            # case x: # Find all values for a microstrip-based circuit
                #This will require a new textwriter method
            case _:
                mode = -1

    # w_h = 2/sqrt(LC)
    # w_0 = 1/sqrt(LC)

    # C = 1/(w_0 * Z_0)
    # L = Z_0 / w_0

    # Table 22.5 gives butterworth values, use equations 31 and 32
    # Table 22.7 gives chebyshev values
            
    filename = f"filters_{int(filter_values.get('f_0'))}Hz_{int(filter_values.get('Z_0'))}Ohm.txt"
    with open(filename, 'w+', newline= '') as textfile:
        for line in text:
            print(line)             # Print each line to the console
            textfile.write(line)    # Print each line to the text file
            textfile.write("\n")    # Add a newline character

    print(f"Transformation values saved to: {filename}")

if __name__ == "__main__":
    main()