#!/usr/bin/python3

"""Base class"""

import json


class Base:
    """ "Defines a Base class"""

    __nb_objets = 0

    def __init__(self, id=None):
        """Initializes the Base class

        Args:
            id (int): The id of the base. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objets += 1
            self.id = Base.__nb_objets

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
