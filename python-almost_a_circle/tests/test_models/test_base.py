import unittest
from models.base import Base
"""Defines test cases for the Base class."""


class test_base(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_auto(self):
        b = Base()
        self.assertEqual(1, b.id)
    
    def test_id_auto_increment(self):
        b = Base()
        self.assertEqual(2, b.id)

    def test_id(self):
        b = Base(89)
        self.assertEqual(89, b.id)

    #def test_to_json_string(self):
        #json_string = Base.to_json_string(None)
        #self.assertEqual(json_string, "[]")

if __name__ == '__main__':
    unittest.main()
