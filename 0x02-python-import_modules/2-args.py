#!/usr/bin/python3
import sys


def main():
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    else:
        if arg_count == 1:
            print("{} argument:".format(arg_count))
        else:
            print("{} arguments:".format(arg_count))

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
