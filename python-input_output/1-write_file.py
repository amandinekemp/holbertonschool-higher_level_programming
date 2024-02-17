#!/usr/bin/python3

"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a file and returns the character count
    Args:
        filename (str): The name of the file. Defaults to "".
        text (str): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
