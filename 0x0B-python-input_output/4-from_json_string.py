#!/usr/bin/python3
"""A function that returns an object in JSON string"""
import json


def from_json_string(my_str):
    """Function will return an object as JSON string

    Args:
        my_str: The JSON string for object

    Returns:
        object: Python data structure represented by JSON string
    """
    return json.loads(my_str)
