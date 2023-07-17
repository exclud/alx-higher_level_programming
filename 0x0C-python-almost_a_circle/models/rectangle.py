#!/usr/bin/python3
"""Classs Rectangle which inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle which inherits from Base which is in the file base.py

    Args:
        Base (): The Class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the object rectangle and the dimensions

        Args:
            width (int): width of the rect
            height (int): height of the rect
            x (int, optional): X axis of the rect. Defaults to 0.
            y (int, optional): Y axis of the rect. Defaults to 0.
            id (int, optional): ID of the rect. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """Getter for x

        Returns:
            int: x axis for rect
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value

        Args:
            value (int): Value of the x value

        Raises:
            TypeError: if input is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y

        Returns:
            int: y axis for rect
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value

        Args:
            value (int): value of y

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return area

        Returns:
            int: area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Visualize the rectangle
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the attr of the rect
        Args:
            *args: Positional arguments.
            **kwargs: The keyword arguments.

        """

        num_args = len(args)
        if num_args > 0:
            self.id = args[0]
        elif kwargs.get('id'):
            self.id = kwargs['id']
        if num_args > 1:
            self.width = args[1]
        elif kwargs.get('width'):
            self.width = kwargs['width']
        if num_args > 2:
            self.height = args[2]
        elif kwargs.get('height'):
            self.height = kwargs['height']
        if num_args > 3:
            self.x = args[3]
        elif kwargs.get('x'):
            self.x = kwargs['x']
        if num_args > 4:
            self.y = args[4]
        elif kwargs.get('y'):
            self.y = kwargs['y']


# if __name__ == '__main__':
#     r = Rectangle(4, 6, 2, 2, 1)
#     print(r)
#     r.display()
