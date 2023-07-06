'''
    filter-calculator.py

    This is a program to help calculate filter transformation values.
    
    Author:     Eleanor Taylor

    Created:    22 June 2023
    Modified:    6 July 2023
    
'''

import txt
import calculate

def main():

    # List of all values tracked by the constant-k section calculators
    constk_keys_list = ["f_0", "w_0", "Z_0", "bw_Hz", "bw_rad",
                 "L_lp", "C_lp", "L_hp", "C_hp", 
                 "L_bp_series", "C_bp_series", "L_bp_parallel", "C_bp_parallel", 
                 "L_bs_parallel", "C_bs_parallel", "L_bs_series", "C_bs_series"]
    # List of all values tracked by the Butterworth calculators
    buttershev_keys_list = ["f_0", "w_0", "Z_0", "bw_Hz", "bw_rad", "n"]

    filter_values = {}

    print ("\n#######################################################################")
    print ("\nWELCOME TO FILTER CALCULATOR - Your one-stop shop for all filter needs!")
    print ("\n#######################################################################\n")

    mode = 0
    mode_string = ""
    while (mode < 1):
        print ("""\nWhich version of the calculator do you want?
        1:  Find all transformaitons from known constant-k LPF values
        2:  Find all transformations for a 50-ohm constant-k transmission line
        3:  Find all transformations for any constant-k transmission line
        4:  Find all transformations for a Butterworth filter
        5:  Find all transformations for a Chebyshev filter\n""")
        
        mode = int(input())

        match mode:
            case 1:
                filter_values = calculate.known_LPF(constk_keys_list)
                text = txt.constk_writer(filter_values)
                mode_string = "known_lpf_constk"
            case 2:
                filter_values = calculate.constk_50ohm(constk_keys_list)
                text = txt.constk_writer(filter_values)
                mode_string = "constk"
            case 3:
                filter_values = calculate.constk(constk_keys_list)
                text = txt.constk_writer(filter_values)
                mode_string = "constk"
            case 4:
                filter_values = calculate.butterworth(buttershev_keys_list)
                text = txt.butterworth_writer(filter_values)
                mode_string = "butterworth"
            case 5:
                filter_values = calculate.chebyshev(buttershev_keys_list)
                text = txt.chebyshev_writer(filter_values)
                mode_string = "chebyshev"
            # case x: # Find all m-derived components with a variable m-value
                #This will require a new textwriter method
            # case x: # Find all m-derived components with a variable m-value and characteristic impedance
                #This will require a new textwriter method
            # case x: # Find all values for a microstrip-based circuit
                #This will require a new textwriter method
            case _:
                mode = -1
            
    for line in text:
        print(line)             # Print each line to the console

    save = (input("Save to text file? (y/n)\t")).lower()
    if (save[0] == "y"):
        filename = f"{mode_string}_{int(filter_values.get('f_0'))}Hz_{int(filter_values.get('Z_0'))}Ohm.txt"
        with open(filename, 'w+', newline= '') as textfile:
            for line in text:
                textfile.write(line)    # Print each line to the text file
                textfile.write("\n")    # Add a newline character
        print(f"Transformation values saved to: {filename}\n")

if __name__ == "__main__":
    main()