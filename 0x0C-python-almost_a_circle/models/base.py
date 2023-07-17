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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON string representation of list_objs to a file

        Args:
            list_objs (list): List of instances inheriting from Base class
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON to dictionary

        Args:
            json_string (str): JSON repr a list of dictionaries

        Returns:
            list: List of dictionaries rep by JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes already set

        Args:
            **dictionary (dict): Keyword arguments representing the attributes

        Returns:
            Base: Instance with attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None
        if dummy_instance is not None:
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a file

        Returns:
            list: List of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                instances = [cls.create(**obj_dict) for obj_dict in json_list]
                return instances
        except FileNotFoundError:
            return []
