#!/usr/bin/python3
"""THIS IS 4-print_square MODULE"""


def print_square(size):
    """PRINTING A SQUARE WITH #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
        
