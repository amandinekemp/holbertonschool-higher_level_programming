#!/usr/bin/python3

"""Module for Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a Square. Inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square. Defaults to 0.
            y (int): The y coordinate of the square. Defaults to 0.
            id (int): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square.

        Args:
            value (int): The size to set for the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
