#!/usr/bin/python3
"""
Contains the matrix_mul function
"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices (lists of lists of integers or floats).
    Args:
        m_a: First matrix.
        m_b: Second matrix.
    Returns:
        The product of the two matrices.
    """
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty and m_b can't be empty")
    
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")
    
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(element)
        result.append(row)
    
    return result

