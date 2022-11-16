#tempConversion.py
"""Conversion functions between farenheit and centigrade"""
# Functions
def centigrade(x):
    return 5*(x-32)/9.0

def farenheit(x):
    return 9*x/5.0 + 32
# constants
Freezing_C = 0.0
Freezing_F = 32.0