#!/usr/bin/python3

"""Unittest for class Rectangle
"""

import unittest
import os
import json
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class test_rectangle(unittest.TestCase):

    def test_rectangle_width_height(self):
        rect = Rectangle(5,15)
        self.assertEqual(1, rect.id)
        self.assertEqual(5, rect.width)
        self.assertEqual(15, rect.height)

    def test_rectangle_all_param(self):
        rect = Rectangle(5,15,3,6,12)
        self.assertEqual(12, rect.id)
        self.assertEqual(5, rect.width)
        self.assertEqual(15, rect.height)
        self.assertEqual(3, rect.x)
        self.assertEqual(6, rect.y)

if __name__ == '__main__':
    unittest.main()
