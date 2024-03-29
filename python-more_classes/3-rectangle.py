#!/usr/bin/python3

"""Represents a rectangle."""


class Rectangle:
    """Rectangle defined by width and height."""
    def __init__(self, width=0, height=0):
        """
        Initialize rectangle.
        Args:
            width: rectangle width
            height: rectangle height
        Raises:
            TypeError: if width or height not integer
            ValueError: if width or height negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get rectangle width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set rectangle width.
        Args:
            value: new width
        Raises:
            TypeError: if value is not int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set rectangle height.
        Args:
            value: new height
        Raises:
            TypeError: if value is not int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate and return rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return (rectangle)
