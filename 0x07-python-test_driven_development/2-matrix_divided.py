#!/usr/bin/python3

"""
This module defines the matrix_divided function.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The input matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testmod()

