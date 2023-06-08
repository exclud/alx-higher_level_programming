#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    add_result = add(a, b)
    sub_result = sub(a, b)
    mult_result = mul(a, b)
    div_result = div(a, b)


    print(f'Addition: {a}+ {b} = {add_result}')
    print(f'Subtraction: {a} - {b} = {sub_result}')
    print(f'Multiplication: {a} * {b} = {mult_result}')
    print(f'Division: {a} / {b} = {div_result}')


if __name__ == "__main__":
    main()
