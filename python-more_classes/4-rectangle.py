#!/usr/bin/python3

"""Module for Rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width (int, optional): The width. Defaults to 0.
            height (int, optional): The height. Defaults to 0.
        """
        self.height = height
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        """Returns a string representation of the rectangle with #."""
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for index in range(self.__height):
            for index2 in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
