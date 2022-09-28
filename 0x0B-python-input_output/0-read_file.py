#!/usr/bin/python3
"""A function 'read_file'"""


def read_file(filename=""):
    """Using with statement to open file"""
    with open("filename", encoding="utf-8") as myFile:
        """Print file"""
        print(myFile.read())
