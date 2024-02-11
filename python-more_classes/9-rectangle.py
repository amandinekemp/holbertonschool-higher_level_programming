#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter."""
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    @classmethod
    def square(cls, size=0):
        """Creates a square rectangle."""
        return Rectangle(size, size)

    def __str__(self):
        """
        Returns a string representation with the character #.

        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Handles deletion."""
        type(self).number_of_instances -= 1
        print("{:s}".format("Bye rectangle..."))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
