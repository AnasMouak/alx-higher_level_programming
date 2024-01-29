#!/usr/bin/python3
"""
N-Queens Solver:

This program finds all solutions for placing N non-attacking queens
on an NxN chessboard.

Usage:
    $ ./101-nqueens.py N

Requirements:
    - N must be an integer greater than or equal to 4.

Attributes:
    - board (list): Represents the chessboard with queens placed.
    - solutions (list): Contains all solutions, each represented as
    [[row, col], [row, col], ...].

In the solutions, each [row, col] pair indicates the position of a queen
on the chessboard.
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the specified position (row, col)
        on the board.

    Args:
    - board (list): The current state of the chessboard.
    - row (int): The row to check.
    - col (int): The column to check.
    - N (int): The size of the chessboard.

    Returns:
    - bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N, solutions):
    """
    Recursively solve the N-Queens problem and store solutions
        in the 'solutions' list.

    Args:
    - board (list): The current state of the chessboard.
    - row (int): The current row being considered.
    - N (int): The size of the chessboard.
    - solutions (list): A list to store the solutions.

    Returns:
    - None
    """
    if row == N:
        solutions.append(list(enumerate(board)))
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens(board, row + 1, N, solutions)


def main(argc, argv):
    """
    Main function to handle command-line arguments and execute
        the N-Queens solver.

    Args:
    - argc (int): The number of command-line arguments.
    - argv (list): The list of command-line arguments.

    Returns:
    - None
    """
    if argc != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        try:
            N = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        board = [-1] * N
        solutions = []
        solve_nqueens(board, 0, N, solutions)

        for solution in solutions:
            print(solution)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
