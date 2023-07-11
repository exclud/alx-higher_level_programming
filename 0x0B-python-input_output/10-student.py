#!/usr/bin/python3
"""Class Student"""


class Student:
    """Student Representation"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student

        Args:
            first_name (str): First Name
            last_name (str): Last Name
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary rep of the student


        """
        return self.__dict__
