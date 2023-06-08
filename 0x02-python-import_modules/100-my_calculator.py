#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    argc = len(sys.argv) - 1
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
