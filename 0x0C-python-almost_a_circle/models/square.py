#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square which inherits from Rectangle

    Args:
        Rectangle (int ): Rectangle which square inherits from
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of square

        Args:
            size (int): size of new square
            x (int, optional):  x cordinate.. Defaults to 0.
            y (int, optional): y cordinate. Defaults to 0.
            id (_type_, optional): identity of new square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print representation of square

        Returns:
            int: square representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
