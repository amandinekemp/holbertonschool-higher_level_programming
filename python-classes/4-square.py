#!/usr/bin/python3

"""Module defining a Square class with a size attribute"""


class Square:

    """Square class representing a geometric square with a size attribute"""

    def __init__(self, size=0):
        """Initializes a square instance with an optional size

        Args:
            size (int): The size of the square, defaults to 0

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the current square's area"""
        return self.__size ** 2
