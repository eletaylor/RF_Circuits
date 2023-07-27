'''
    txt.py

    This file acts as a library of text functions for different types of amplifiers to
    display their output in a user-friendly manner.
    
    Author:     Eleanor Taylor

    Created:     26 July 2023
    Modified:    26 July 2023
    
'''

def tuned_writer(amplifier):

    table_lines = ""
    for i in range(len(amplifier.get("R_C"))):
        L = "{:.2e}".format(amplifier.get("L")[i])
        C = "{:.2e}".format(amplifier.get("C")[i])
        R_E = int(amplifier.get("R_E")[i])
        R_C = int(amplifier.get("R_C")[i])
        
        table_lines += (f"\t{R_C}\t\t{R_E}\t\t{L}\t{C}\n")

    text = [
        f"\n##########################################################################\n",
        f"Values for a tuned amplifier with:",
        f"  Center frequency:\t{amplifier.get('f_r')} Hz",
        f"  Bandwidth:\t\t{amplifier.get('bw')} Hz",
        f"  Quality factor:\t{amplifier.get('Q')}",
        f"  Decibel gain:\t\t{amplifier.get('gain_dB')}\n",
        f"##########################################################################\n",
        f"\tRc (Ohms)\tRe (Ohms)\tL (H)\t\tC (F)",
        f"{table_lines}",
        f"##########################################################################\n"
        ]
    
    return text

def feedback_writer(amplifier):     #TODO: IMPLEMENT!

    table_lines = ""

    text = [
        f"\n##########################################################################\n",
        f"Values for a feedback amplifier with:",
        f"  Center frequency:\t{amplifier.get('f_r')} Hz",
        f"  Bandwidth:\t\t{amplifier.get('bw')} Hz",
        f"  Quality factor:\t{amplifier.get('Q')}\n",
        f"##########################################################################\n",
        f"{table_lines}",
        f"\n##########################################################################\n"
        ]
    
    return text