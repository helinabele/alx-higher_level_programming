#!/usr/bin/python3
"""THIS IS 3-say_my_name MODULE"""


def say_my_name(first_name, last_name=""):
    """PRINTING MY FIRSTNAME AND LASTNAME"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
    
