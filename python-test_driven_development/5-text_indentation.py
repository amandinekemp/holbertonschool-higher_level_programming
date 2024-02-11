#!/usr/bin/python3

"""Prints a text with 2 new lines after . ? and :"""


def text_indentation(text):
    """Prints a text with new lines after . ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
