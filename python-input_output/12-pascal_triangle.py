#!/usr/bin/python3

"""Generates Pascal's triangle up to n lines."""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n lines.

    Args:
        n (int): The number of lines in Pascal's triangle.

    Returns:
        list: Pascal's triangle up to n lines.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for line_number in range(1, n):
        row = [1]
        for j in range(1, line_number):
            row.append(triangle[line_number-1][j-1] + triangle[line_number-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
