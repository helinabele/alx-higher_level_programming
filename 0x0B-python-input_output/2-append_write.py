#!/usr/bin/python3
"""A function 'append_write'"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, "a", encoding='utf-8') as myFile:
        return myFile.write(text)
