#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result.

    Args:
    - m_a (numpy.ndarray): The first matrix represented as a NumPy array.
    - m_b (numpy.ndarray): The second matrix represented as a NumPy array.

    Returns:
    - numpy.ndarray: The product matrix as a NumPy array.
    """
    return (np.matmul(m_a, m_b))
