#!/usr/bin/python3

"""Module for Rectangle class."""


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
            Args:
            width (int, optional): Rectangle width. Defaults to 0.
            height (int, optional): Rectangle height. Defaults to 0.

            Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the rectangle width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the rectangle width.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the rectangle height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the rectangle height.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a '#' representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle instance."""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Handles actions upon rectangle deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
