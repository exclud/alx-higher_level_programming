#!/usr/bin/python3
"""A function to write an object to a text file using JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file using JSON rep

    Args:
        my_obj (): Object to serialize
        filename (): Name of file to be written
    """
    with open(filename, 'w') as o:
        json.dump(my_obj, o)
