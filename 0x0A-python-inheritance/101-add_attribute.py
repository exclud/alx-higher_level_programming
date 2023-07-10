#!/usr/bin/python3
"""function for new attr to object"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr (str): The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object doesn't support attribute assignment.

    """
    if '__dict__' in dir(obj):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
