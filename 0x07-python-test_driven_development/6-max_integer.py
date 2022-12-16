#!/usr/bin/python3
"""THIS IS 6-max_integer MODULE"""


def max_integer(list=[]):
    """MAX INTEGER IN A LIST OF INTEGER"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


