#!/usr/bin/python3
"""THIS IS 0-add_integer MODULE"""

def add_integer(a, b=98):
    """ADDITION OF a AND b"""
    
    if type(a) is not int and type(a) is not float:
        raise TypeError ("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError ("b must be an integer")
    
    if type(a) is float:
        a = int(a)
        if type(b) is float:
            b = int(b)
    return a+b
