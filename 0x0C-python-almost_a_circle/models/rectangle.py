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
    def width(self, value):
        """Getter for the width attribute

        Args:
            value (int): the value  of the width

        Returns:
            int: returns the width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for width attribute
        Args:
            value (int): Width to set
        Raises:
            ValueError: If width val is not +ve int
        """
        self.__validate_positive_int("width", value)
        self.__width = value
        
    @property
    def height(self):
        """Getter for the height attribute

        Returns:
            int: height of rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for the height attribute

        Args:
            value (int): Height to set
        Raises:
        ValueError: If height is not positive
        """
        self.__validate_positive_int("height", value)
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
        """Setter for the x attribute

        Args:
            value (int): value of x
        Raises:
            ValueError : if x is not a +ve int
        """
        self.__validate_positive_int("x", value)
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
        """Setter for the y attribute

        Args:
            value (int): value of y
        Raises:
            ValueError : if y is not a +ve int
        """
        self.__validate_positive_int("y", value)
        self.__y = value

    def __validate_positive_int(self, attribute, value):
        """Raises Value Error if int is not positive

        Args:
            attribute (str): name of attribute being validated e.g height
            value (int): Value to validate

        Raises:
            ValueError: if the value is not a +ve int
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{attribute} must be a positive integer")
    
    def area(self):
        """Calculate and return area

        Returns:
            int: area of rectangle
        """
        return self.width *self.height
    
    def display(self):
        """Visualize the rectangle
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


# if __name__ == '__main__':
#     r = Rectangle(4, 6, 2, 2, 1)
#     print(r)
#     r.display()
