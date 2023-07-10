#!/usr/bin/python3
def lookup(obj):
    """A function that returns the list of avail attributes and methods

    Args:
        obj : The object to check

    Returns:
        list: List containing attributes and methods
    """
    return dir(obj)
