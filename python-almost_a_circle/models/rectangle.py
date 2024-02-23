#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle.

        Args:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
           x (int): The x coordinate of the rectangle. Defaults to 0.
           y (int): The y coordinate of the rectangle. Defaults to 0.
           id (int): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width to set for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height to set for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the rectangle.

        Args:
            value (int): The x coordinate to set for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the rectangle.

        Args:
            value (int): The y coordinate to set for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculates and returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance to stdout using the '#' character."""
        for column in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x + self.__width * "#")

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        s_id = self.id
        s_x = self.__x
        s_y = self.__y
        s_wid = self.__width
        s_hei = self.__height
        return f"[Rectangle] ({s_id}) {s_x}/{s_y} - {s_wid}/{s_hei}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute: id, width, height, x, y.

        Args:
            args (int): Todo
            kwargs (int): Todo
        """
        if args:
            attributs = ["id", "width", "height", "x", "y"]
            for index, arg in enumerate(args):
                if index < len(attributs):
                    setattr(self, attributs[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance."""
        return {
            "x": self.__x,
            "width": self.__width,
            "id": self.id,
            "height": self.__height,
            "y": self.__y,
        }
