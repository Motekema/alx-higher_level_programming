#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    old_matrix = matrix.copy()

    for i in range(len(matrix)):
        old_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (old_matrix)
