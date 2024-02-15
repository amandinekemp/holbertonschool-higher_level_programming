#!/usr/bin/python3

"""Defines a basic geometric shape."""


class BaseGeometry:
    """Represents a basic geometric shape."""
    def area(self):
        """Raises an Exception with message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
