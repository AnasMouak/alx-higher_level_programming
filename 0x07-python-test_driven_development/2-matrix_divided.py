#!/usr/bin/python3
"""
Module provides a function for dividing elements of a matrix
by a given divisor.

Module: matrix_divider

Functions:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor
    and returns the result.

    Parameters:
    - matrix (list of lists): The matrix to be divided,
                            where each element is an integer or float.
    - div (int or float): The divisor used for division.

    Returns:
    list of lists: A new matrix where each element is the result
                    of dividing the corresponding element
                    in the input matrix by the divisor.
                    The result is rounded to two decimal places.

    Raises:
    TypeError: If the input matrix is not a valid matrix (list of lists)
                containing only integers or floats, if the rows of the matrix
                are not of equal length, or if the divisor is not a number.
    ZeroDivisionError: If the divisor is 0.
    """
    if not all(isinstance(i, list) and
               all(isinstance(j, (int, float)) for j in i) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    elif any(len(matrix[0]) != len(i) for i in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    matrixCopy = [row[:] for row in matrix]
    for i in range(len(matrixCopy)):
        for j in range(len(matrixCopy[i])):
            matrixCopy[i][j] = round(matrixCopy[i][j] / div, 2)

    return matrixCopy
