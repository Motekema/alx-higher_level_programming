#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, col in enumerate(row):
            print("{:d}".format(col), end=" " if index < len(row) - 1 else "")
        print()
