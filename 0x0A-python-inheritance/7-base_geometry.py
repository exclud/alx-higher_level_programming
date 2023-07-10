#!/usr/bin/python3
"""An Empty Class BaseGeometry"""


class BaseGeometry:
    """Class for geometry calculations
    """
    def area(self):
        """Area Calculations

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value

        Args:
            name (string): name of value
            value (int): value to validate

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
