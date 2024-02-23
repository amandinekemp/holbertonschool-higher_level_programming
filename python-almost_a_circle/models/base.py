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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(cls.__name__ + ".json", 'w') as file:
            file.write(cls.to_json_string(list_dicts))
