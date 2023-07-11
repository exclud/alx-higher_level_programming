#!/usr/bin/python3
"""A function that writes a string text to a file"""
def write_file(filename="", text=""):
    """Function to write string text to a file

    Args:
        filename (str, optional): Name of the filename. Defaults to "".
        text (str, optional): Text to be written in the file. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open (filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
