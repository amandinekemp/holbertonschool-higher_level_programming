#!/usr/bin/python3

"""Unittest for class Square"""

import unittest
import os
import json

from models.square import Square


class test_square(unittest.TestCase):

    def test_square_exists(self):
        """Test if an instance of Square can be created with size 1."""
        s = Square(1)
        self.assertIsInstance(s, Square)


if __name__ == "__main__":
    unittest.main()
