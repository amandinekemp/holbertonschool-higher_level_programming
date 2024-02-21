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

    def test_to_json_string_None(self):
        self.assertEqual("[]", Base.to_json_string(None))




    def test_id_negative(self):
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        b = Base((8,))
        self.assertEqual((8,), b.id)

if __name__ == '__main__':
    unittest.main()
