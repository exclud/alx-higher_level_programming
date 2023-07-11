#!/usr/bin/python3
"""Add all args to a python list and save them to fiel"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


def main():
    """Add all args to a python list
    """
    list_of_args = []

    for arg in sys.argv[1]:
        list_of_args.append(arg)

    json_data = {"args": list_of_args}

    save_to_json_file(json_data, "add_item.json")


if __name__ == "__main__":
    main()
