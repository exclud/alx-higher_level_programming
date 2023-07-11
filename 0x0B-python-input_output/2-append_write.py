#!/usr/bin/python3
"""A function to append a string to a text file"""


def append_write(filename="", text=""):
    """Function which appends a string to a text file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): The text to be appended. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.seek(0, 2)
        num_chars_added = file.write(text)
    return num_chars_added
