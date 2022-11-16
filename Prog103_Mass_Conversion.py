#massconversion.py
"""Conversion of Masses"""

#Functions
def kgtotonne(x):
    """Conversion from Kilogram to tonne"""
    return x * 0.001

def tonnetokg(x):
    """Conversion from Tonne to Kilogram"""
    return x/0.001

def kgtopound(x):
    """Conversion from Kilogram to Pounds"""
    return x * 2.20462

def poundtokg(x):
    """Conversion from Pounds to Kilogram"""
    return x/2.20462

# Constants
KtT = 0.001
KtP = 2.20462
