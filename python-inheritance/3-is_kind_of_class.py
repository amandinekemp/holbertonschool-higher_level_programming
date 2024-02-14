#!/usr/bin/python3

"""Checks if an object is an instance of a class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or its subclasses.
    Parameters:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
    True if object is an instance of a_class or its subclasses, else False.
    """
    return isinstance(obj, a_class)
