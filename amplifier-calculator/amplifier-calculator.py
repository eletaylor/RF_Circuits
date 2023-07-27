'''
    filter-calculator.py

    This is a program to help calculate filter transformation values.
    
    Author:     Eleanor Taylor

    Created:    26 July 2023
    Modified:   26 July 2023
    
'''

import txt
import calculate

def main():

    keys_list = ["f_r", "w_r", "bw", "bw_rad", "Q", "L", "C", "R"]

    print ("\n################################################################################")
    print ("\nWELCOME TO AMPLIFIER CALCULATOR - Your one-stop shop for all RF amplifier needs!")
    print ("\n################################################################################\n")

    mode = 0
    
    while (mode < 1):

        print ("""\nWhich version of the calculator do you want?
        1:  Find values for a tuned amplifier
        2:  Find values for a feedback amplifier [COMING SOON!]
        3:  Find values for a general BJT amplifier [COMING SOON!]\n""")
        
        mode = int(input())
        mode_string = ""
        
        match mode:
            case 1:
                amplifier = calculate.tuned(keys_list)
                text = txt.tuned_writer(amplifier)
                mode_string = f"tuned_amplifier_{int(amplifier.get('f_r'))}Hz"
            case 2:
                amplifier = calculate.feedback(keys_list)
                text = txt.feedback_writer(amplifier)
                mode_string = "feedback_amplifier"
            case _:
                mode = -1

     # Print each line to the console       
    for line in text:
        print(line)

    save = (input("Save to text file? (y/n)\t")).lower()    # Ask if the user wants to save their data
    if (save[0] == "y"):
        filename = f"{mode_string}.txt"
        with open(filename, 'w+', newline= '') as textfile:
            for line in text:
                textfile.write(line)    # Print each line to the text file
                textfile.write("\n")    # Add a newline character
        print(f"Transformation values saved to: {filename}\n")
    else:
        print("\n")

if __name__ == "__main__":
    main()