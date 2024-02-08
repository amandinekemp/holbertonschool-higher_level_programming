#!/usr/bin/python3

"""Module defining a Square class with a size attribute"""


class Square:

    """Square class that represents a square with a size attribute"""

    def __init__(self, size=0):
        """Initializes a square instance with an optional size

        Args:
            size (int): The size of the square, defaults to 0

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
