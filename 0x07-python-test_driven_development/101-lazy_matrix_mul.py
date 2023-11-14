#!/usr/bin/python3
"""
Defines lazy_matrix_mul function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Calculates the matrix multiplication of two matrices using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying m_a and m_b.

    """
    return numpy.matmul(m_a, m_b)

