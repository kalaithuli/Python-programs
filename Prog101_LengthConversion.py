#lengthconversion.py
"""Conversion of Lengths"""

#Functions
def miletokm(x):
    """Conversion from Mile to Kilometer"""
    return x * 1.609344

def kmtomile(x):
    """Conversion from Kilometer to Mile"""
    return x/1.609344

def feettinches(x):
    """Conversion from Feet to Inches"""
    return x * 12

def inchestofeet(x):
    """Conversion from Inches to Feet"""
    return x/12

# Constants
MtK = 1.609344
FtI = 12