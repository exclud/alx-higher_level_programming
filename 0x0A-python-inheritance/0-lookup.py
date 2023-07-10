#!/usr/bin/python3
def lookup(obj):
    """A function that returns the list of available attributes and methods

    Args:
        obj (int): the object

    Returns:
        _type_: _description_
    """
    attributes = []
    methods = []
    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        if callable(attribute):
            methods.append(attribute_name)
        else:
            attributes.append(attribute_name)
    return attributes + methods
