#!/usr/bin/python3
"""A function 'read_file'"""


def read_file(filename=""):
    """Using with statement to open file"""
    with open(filename, "r", encoding="utf-8") as f:
        """Print file"""
        print(f.read(), end="")
