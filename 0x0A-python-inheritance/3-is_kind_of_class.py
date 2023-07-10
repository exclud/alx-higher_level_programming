#!/usr/bin/python3
"""A function to check the status of the inheritance"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is an instance or inherited instance of a class

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
       True: If object is intance of a class
       False: If object !instance of class inherited from specified class

    """
    return isinstance(obj, a_class)
