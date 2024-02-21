"""Defines test cases for the Base class."""

import unittest, json
from models.base import Base


class test_Base(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_none(self):
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

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
