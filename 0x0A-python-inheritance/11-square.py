#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize new square.

        Args:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
