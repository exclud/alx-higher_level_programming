#!/usr/bin/python3
"""A function that returns a list of integers representing Pascals Triangle"""


def pascal_triangle(n):
    """Pascal's Triangle

    Args:
        n (int): integers representing the pascal's triangle

    Returns:
       int: list of lists of ints
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n + 1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
