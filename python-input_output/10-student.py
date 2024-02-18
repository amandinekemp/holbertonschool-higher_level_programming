#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, sttrs=None):
        """Returns a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attributes to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if sttrs is None:
            return self.__dict__
        else:
            dict = {}
            for key in sttrs:
                if key in self.__dict__:
                    dict[key] = self.__dict__[key]
            return dict
