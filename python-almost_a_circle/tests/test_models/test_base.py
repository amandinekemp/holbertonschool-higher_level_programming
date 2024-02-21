"""Defines test cases for the Base class."""

import unittest, json
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_none(self):
        """Sending no id"""
        b = Base()
        self.assertEqual(1, b.id)
        
    def test_passed_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)


if __name__ == '__main__':
    unittest.main()
