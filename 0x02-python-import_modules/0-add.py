#!/usr/bin/python3
from add_0 import add


def main():
    a = 1
    b = 2
# result = add(a, b)
    print("{} + {} = {}\n".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()
