#!/usr/bin/python3

"""Defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """
        Initializes a Square with a size.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        Rectangle.__init__ = (self, size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square's description."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
