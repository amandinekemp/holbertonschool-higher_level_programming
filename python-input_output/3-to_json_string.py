#!/usr/bin/python3

"""Defines a function that returns the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj (Any): The object to convert to JSON.

    Returns: The JSON representation of the object.
    """
    return json.dumps(my_obj)
