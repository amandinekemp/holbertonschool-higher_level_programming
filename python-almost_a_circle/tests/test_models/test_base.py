import unittest, json
from models.base import Base
"""Defines test cases for the Base class."""


class test_base(unittest.TestCase):
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

    def test_to_json_string_None(self):
        """Test if to_json_string returns '[]' when passed None."""
        self.assertEqual(Base.to_json_string(None), '[]')


if __name__ == '__main__':
    unittest.main()
