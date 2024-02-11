#!/usr/bin/python3

"""Rectangle defined by width and height."""


class Rectangle:
    """Define a rectangle with the given width and height."""
    def __init__(self, width=0, height=0):
        """
        Initialize rectangle.
        :param width: rectangle width
        :param height: rectangle height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Get rectangle width. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set rectangle width.
        :param value: new width
        :raises TypeError: if value is not int
        :raises ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get rectangle height. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set rectangle height.
        :param value: new height
        :raises TypeError: if value is not int
        :raises ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
