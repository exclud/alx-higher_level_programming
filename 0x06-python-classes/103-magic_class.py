#!/usr/bin/python3
"""
Defination of Class MagicClass.
"""

import math


class MagicClass:
    """Class Representation"""
    def __init__(self, radius=0):
        """"Class Initialization
        Arg: radius: radius of new MagicClass"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Return are of MagicClass"""
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """Return Circumfrence of MagicClass"""
        return 2 * math.pi * self.__radius
