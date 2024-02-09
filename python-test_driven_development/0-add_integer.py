#!/usr/bin/python3

"""Function that performs addition of 2 integers"""


def add_integer(a, b=98):
    """
    Adds two numbers (integers or floats) and returns the result as an integer

    Parameters:
    a (int or float): The first number to add
    b (int or float): The second number to add. The default value is 98

    Returns:
    int: The sum of a and b as an integer

    Raises:
    TypeError: If a or b is not an integer or float
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
