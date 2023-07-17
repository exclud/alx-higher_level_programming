#!/usr/bin/python3
"""Base model Class"""
import json


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
      
    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to JSON

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
