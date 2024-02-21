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

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0# type: ignore

if __name__ == '__main__':
    unittest.main()
