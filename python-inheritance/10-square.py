#!/usr/bin/python3

"""Defines a class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """
        Initialize a new square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", size)
        self().__init__ = (size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
