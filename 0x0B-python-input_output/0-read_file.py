#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Function that read a text file

    Args:
        filename (str, optional): The filename. Defaults to "".
    """
    with open(filename, "r", encoding='utf-8') as file:
        contents = file.read()
        print(contents)
