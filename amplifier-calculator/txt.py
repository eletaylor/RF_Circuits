'''
    txt.py

    This file acts as a library of text functions for different types of amplifiers to
    display their output in a user-friendly manner.
    
    Author:     Eleanor Taylor

    Created:     26 July 2023
    Modified:    26 July 2023
    
'''

def tuned_writer(amplifier):    # TODO: IMPLEMENT

    text = [
        f"\n##########################################################################\n",
        f"Values for a tuned amplifier with:",
        f"  Center frequency:\t\t\t{amplifier.get('f_r')} Hz",
        f"  Bandwidth:\t\t{amplifier.get('bw')} Hz",
        f"\n##########################################################################\n",
        ]
    
    return text