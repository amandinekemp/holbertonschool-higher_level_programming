#!/usr/bin/python3

"""Module defining a Square class with a size attribute"""


class Square:

    """Square class representing a geometric square with a size attribute"""

    def __init__(self, size=0):
        """Initializes a square instance with an optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the current square's area"""
        return self.__size ** 2
