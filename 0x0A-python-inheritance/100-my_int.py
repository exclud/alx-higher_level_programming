#!/usr/bin/python3
"""Class that inherits from int"""


class MyInt(int):
    """
    Class representing a rebellious integer, MyInt.
    """

    def __eq__(self, other):
        """
        Override the == operator.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.

        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.

        """
        return super().__eq__(other)
