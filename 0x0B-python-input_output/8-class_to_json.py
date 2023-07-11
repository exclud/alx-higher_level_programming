#!/usr/bin/python3
""""Return dictionary description"""


def class_to_json(obj):
    """Return dict description

    Args:
        obj (obj): object to serialize

    Returns:
        json_data: dictionary that can be used to serialize the obj to JSON
    """
    json_data = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_data[key] = value
        else:
            json_data[key] = class_to_json(value)

    return json_data
