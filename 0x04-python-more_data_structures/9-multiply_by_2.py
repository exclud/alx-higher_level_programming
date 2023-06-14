#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary

# def multiply_by_2(a_dictionary):
#     return {k : v * 2 for k, v in a_dictionary.items()}
