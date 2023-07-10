#!/usr/bin/python3
"""Function to check if object is instance of inherited class"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited (directly or indirectly) from the specified
        class; False otherwise.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
