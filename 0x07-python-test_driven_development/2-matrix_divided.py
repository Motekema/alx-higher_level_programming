#!/usr/bin/python3
"""
This is "2-matrix_divided" module.

2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements in the matrix by div.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor to divide the elements by.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to zero.

    """
    if type(matrix) is not list:
        raise TypeError("matrix must be matrix (list of lists) of integers/floats")
    
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError("matrix must be matrix (list of lists) of integers/floats")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be matrix (list of lists) of integers/floats")
    
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(i / div, 2) for i in l] for l in matrix]

