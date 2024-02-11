#!/usr/bin/python3

"""Module for Rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height.

            Args:
                width: rectangle width
                height: rectangle height

            Raises:
                TypeError: if width or height not integer
                ValueError: if width or height negative
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width, ensuring it's a positive integer."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height, ensuring it's a positive integer."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
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
