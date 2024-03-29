#!/usr/bin/python3

""" Function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix.

    Parameters:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): number by which to divide all elements of the matrix

    Returns:
        list of lists of float: A new matrix with all elements divided by div,
            rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
            if each row of the matrix does not have the same size,
            or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    mess_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(mess_error)
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(mess_error)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
