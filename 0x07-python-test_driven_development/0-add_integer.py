#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Add Two integers

    Args:
        a (int or floar): the first number
        b (int or float): second number. Defaults to 98.

    Raises:
        TypeError: if a is not an integer or float
        TypeError: if a is not an integer or float

    Returns:
        int: the sum of the two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(a, float):
        b = int(b)
    
    return a+b
