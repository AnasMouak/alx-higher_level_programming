#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = list(map(lambda i: list(map(lambda x: x**2, i)), matrix))
    return matrix
