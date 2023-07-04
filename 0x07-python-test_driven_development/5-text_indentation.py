#!/usr/bin/python3


def text_indentation(text):
    """
    Print a text with 2 new lines after each occurrence of '.', '?', and ':'

    Args:
        text (str): The input text

    Raises:
        TypeError: If the text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        result += char

        # Check for punctuation marks and add new lines
        if char in ['.', '?', ':']:
            result += "\n\n"

    # Print the formatted text
    print(result.strip())
