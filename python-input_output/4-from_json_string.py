#!/usr/bin/python3

"""Defines a function that returns an object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to represent.

    Returns: The object represented by the JSON string.
    """
    return json.loads(my_str)
