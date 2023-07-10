#!/usr/bin/python3
"""An object defination which looks up a class"""


def lookup(obj):
    """A function that returns the list of avail attributes and methods

    Args:
        obj : The object to check

    Returns:
        list: List containing attributes and methods
    """
    return dir(obj)
