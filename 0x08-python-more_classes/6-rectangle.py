#!/usr/bin/python3
"""Defination of a class Rectangle"""


class Rectangle:
    """Class Rectangle defination
    Attributes:
        width (int): Width of the rectangle
        height (int): The height o f the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """

        Raises:
            TypeError : If width !> integer
            ValueError : If width < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The width to set "value"

        Raises:
        TypeError: If value is ! integer.
        ValueError: If value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int : The height of the rectangle

        Raises:
            TypeError: If height ! integer
            ValueError: If height < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of rectangle

        Args:
            value (int): The value of the height to set

        Raises:
            TypeError: If value ! integer
            ValueError : If value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate area and return it.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate perimeter and return it.

        Returns:
            int : Perimeter of Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Return String Representation of the rectangle

        Returns:
        str: String rep of rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print the message when an instance of Rectangle is deleted
        Decrements the number_of_instances class attribute
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
