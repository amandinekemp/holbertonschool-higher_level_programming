#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        square = []
        for index in row:
            square.append(index ** 2)
        result.append(square)
    return result
