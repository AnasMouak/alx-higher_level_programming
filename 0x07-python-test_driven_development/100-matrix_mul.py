#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
    - m_a (list): The first matrix represented as a list of lists.
    - m_b (list): The second matrix represented as a list of lists.

    Returns:
    - list: The product matrix as a list of lists.

    Raises:
    - TypeError: If m_a or m_b is not a list, or if m_a/m_b is not a list of
        lists.
    - ValueError: If m_a or m_b is empty or contains empty lists, or if the
        matrices can't be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    elif m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all(isinstance(m_a, list) and 
                 all(isinstance(j, (int,float)) for j in i)for i in m_a):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(isinstance(m_b, list) 
                 and all(isinstance(j, (int,float)) for j in i)for i in m_b):
        raise TypeError("m_b should contain only integers or floats")
    elif any(len(m_a[0]) != len(i) for i in m_a[1:]):
        raise TypeError("Each row of the m_a must have the same size")
    elif any(len(m_b[0]) != len(i) for i in m_b[1:]):
        raise TypeError("Each row of the m_b must have the same size")
    elif len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    c = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                c[i][j] += m_a[i][k] * m_b[k][j]
    return c
