#!/usr/bin/python3
"""Class that Inherits from list"""


class MyList(list):
    """Class which inherits from list

    Args:
        list(int) : The one which is being inherited
    """
    def print_sorted(self):
        """_prints the list sorted in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
