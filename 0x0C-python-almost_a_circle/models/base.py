#!/usr/bin/python3
"""Base model Class"""


class Base:
    """Base Class for managing id attributes in other classes
    Attributes:
        __nb_objects (int): Keep track of the number of objects created
        id (int): Reps unique identifier
    Methods:
        __init__(self, id=None): Initialize the object with unique id
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize the Base Class with a unique id

        Args:
            id (int, optional): Unique identifier for object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
