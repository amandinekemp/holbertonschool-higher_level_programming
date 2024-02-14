#!/usr/bin/python3

"""Checks if an object is an instance of a subclass of a specified class."""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a subclass of a specific class.

    Parameters:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
    True if object is an instance of a subclass of a_class, else False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
