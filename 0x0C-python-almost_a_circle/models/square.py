#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate position. Defaults to 0.
            y (int): Y-coordinate position. Defaults to 0.
            id (int): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): Size of the square.

        Raises:
            ValueError: If the value is less than or equal to 0.
            TypeError: If the value is not an integer.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: List of arguments (no-keyworded).
                1st argument: id attribute.
                2nd argument: size attribute.
                3rd argument: x attribute.
                4th argument: y attribute.
            **kwargs: Double pointer to a dictionary (keyworded arguments).
                Each key represents an attribute to the instance.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the rectangle.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
