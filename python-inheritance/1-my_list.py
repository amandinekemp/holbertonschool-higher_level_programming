#!/usr/bin/python3

"""Inherits from list and adds print_sorted method."""


class MyList(list):
    """Sorts and prints the list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
