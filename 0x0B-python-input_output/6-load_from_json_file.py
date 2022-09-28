#!usr/usr/bin/python3
"""A 'load_from_json_file' function"""
import json


def load_from_json_file(filename):
    """create an Object from a “JSON file”"""
    with open(filename) as myFile:
        return json.load(myFile)

