#!/usr/bin/python3
"""Function to check if object is instance of inherited class"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of class inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True:if object is nstance of a class that inherited from the specified
        class; False otherwise.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
