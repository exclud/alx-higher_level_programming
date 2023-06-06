#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:  # If the character is a lowercase letter
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
