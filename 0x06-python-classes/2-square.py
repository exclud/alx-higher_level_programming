#!/usr/bin/python3
class Square:
    """
    This class represents a square
    """
    def __init__(self, size=0):
        """
        Initialize a square with the size given
        Args:
        size :The size of the square
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
