#!/usr/bin/python3

"""Checks if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Determines if an object is an instance of a specific class.

    Parameters:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
