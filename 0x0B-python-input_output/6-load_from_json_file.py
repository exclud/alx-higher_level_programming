#!/usr/bin/python3
"""Function to create an Object from JSON file"""
import json


def load_from_json_file(filename):
    """Create an object from JSON file

    Args:
        my_obj (): The Object
        filename (): Name of file to read

    Returns:
        data: object representation
    """
    with open(filename, 'r') as o:
        data = json.load(o)
    return data
