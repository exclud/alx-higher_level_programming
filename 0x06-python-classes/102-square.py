#!/usr/bin/python3
class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int or float): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int or float): The size to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have equal areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares have different areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
