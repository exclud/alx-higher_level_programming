#!/usr/bin/python3
"""Function which checks if object is an exact instance of class"""


def is_same_class(obj, a_class):
    """Function to check if object is an exacr instance of class

    Args:
        obj : The object to be checked
        a_class (type): The specified class to do the comparison

    Returns:
        True: If object is exact instance of a class
        False: If object is not exacttly an insrance of the class
    """
    if type(obj) == a_class:
        return True
    return False
