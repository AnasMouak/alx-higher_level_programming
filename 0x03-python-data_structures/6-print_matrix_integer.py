#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, val in enumerate(i):
            print("{:d}".format(val), end=" " if j < len(i) - 1 else "")
        print()
