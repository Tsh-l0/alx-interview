#!/usr/bin/python3
"""
Pascal's Triangle
This function return a list of lists representing the Triangle of n
"""


def pascal_triangle(n):
    """
    Generates the triangle up to n rows

    Args:
        n: The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for a in range(1, n):
        p_row = triangle[-1]
        n_row = [1]

        for ab in range(1, len(p_row)):
            n_row.append(p_row[ab - 1] + p_row[ab])

        n_row.append(1)
        triangle.append(n_row)

    return triangle
