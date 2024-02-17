#!/usr/bin/python3

"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a file and returns the number of characters added.

    Args:
        filename (str): The name of the file. Defaults to "".
        text (str): The text to append to the file. Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        return file.write(text)
