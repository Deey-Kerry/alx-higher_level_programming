#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers"""
    new_matx = matrix.copy()

    for i in range(len(matrix)):
        new_matx[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_matx)
