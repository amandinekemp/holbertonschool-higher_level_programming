#!/usr/bin/python3

"""Defines a function that writes an object to a text file in JSON format"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj (Any): The object to write to the file.
        filename (str): The name of the file.
    """
    with open(filename, "w") as file:
        json_objet = json.dumps(my_obj)
        file.write(json_objet)
        file.clode()
