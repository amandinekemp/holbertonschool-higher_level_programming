#!/usr/bin/python3

"""Defines a function that returns the dictionary description for
JSON serialization of an object."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization.

    Args:
        obj (Any): An instance of a class.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
