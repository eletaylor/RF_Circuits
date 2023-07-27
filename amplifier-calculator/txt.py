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
    for i in range(len(amplifier.get("L")) - 1):
        L = amplifier.get("L")[i]
        C = amplifier.get("C")[i]
        R = amplifier.get("R")[i]
        table_lines += (f"\t{L}\t\t{C}\t{R}\n")

    text = [
        f"\n##########################################################################\n",
        f"Values for a tuned amplifier with:",
        f"  Center frequency:\t{amplifier.get('f_r')} Hz",
        f"  Bandwidth:\t\t{amplifier.get('bw')} Hz",
        f"  Quality factor:\t{amplifier.get('Q')}\n",
        f"##########################################################################\n",
        f"\tL (H)\t\tC (F)\t\tR (Ohms)",
        f"{table_lines}",
        f"\n##########################################################################\n"
        ]
    
    return text