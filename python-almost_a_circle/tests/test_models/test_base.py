#!/usr/bin/python3

import unittest, json
from models.base import Base

"""Defines test cases for the Base class."""


class TestBase(unittest.TestCase):
	"""Tests for the Base class."""

    def test_id_none(self):
        """Sending no id"""
        b = Base()
        self.assertEqual(1, b.id)


if __name__ == '__main__':
    unittest.main()