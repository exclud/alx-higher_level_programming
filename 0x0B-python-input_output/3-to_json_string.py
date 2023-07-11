#!/usr/bin/python3
"""Function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """Return JSON Representation of an object string

    Args:
        my_obj (_type_): The object to convert to JSON

    Returns:
        str: JSON representation of an object
    """
    return json.dumps(my_obj)
