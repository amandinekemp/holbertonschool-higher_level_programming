#!/usr/bin/python3

"""Base class tests"""

import json


class Base:
    """"Defines a Base class"""
    __nb_objets = 0

    def __init__(self, id=None):
        """ Initializes the Base class

        Args:
            id (int): The id of the base. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objets += 1
            self.id = Base.__nb_objets
