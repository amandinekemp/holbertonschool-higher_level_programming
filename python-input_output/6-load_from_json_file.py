#!/usr/bin/python3

"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the file.

    Returns:
        Any: The object created from the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
