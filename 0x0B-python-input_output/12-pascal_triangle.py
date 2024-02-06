#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - list of lists: A list containing the rows of Pascal's triangle
                     up to the nth row.
                     Each row is represented as a list of integers.
    """
    if n <= 0:
        return []
    if isinstance(n, int):
        result = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            row.append(1)
            result.append(row)
        return result
