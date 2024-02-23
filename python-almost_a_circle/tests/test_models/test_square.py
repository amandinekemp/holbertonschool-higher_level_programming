import unittest
import os
import json
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_to_dictionary(self):
        s = Square(10, 3, 4, 8)
        expected_output = {'id': 8, 'size': 10, 'x': 3, 'y': 4}
        self.assertDictEqual(s.to_dictionary(), expected_output)

    def test_square_creation(self):
        self.assertEqual(Square(5).size, 5)
        self.assertEqual(Square(5, 3).x, 3)
        self.assertEqual(Square(5, 3, 2).y, 2)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(TypeError):
            Square(5, "3")
        with self.assertRaises(TypeError):
            Square(5, 3, "2")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -3)
        with self.assertRaises(ValueError):
            Square(5, 3, -2)
        with self.assertRaises(ValueError):
            Square(0, 10).size

    def test_str(self):
        square = Square(7, 6, 5, 4)
        expected_output = '[Square] (4) 6/5 - 7'
        self.assertEqual(str(square), expected_output)

    def test_update(self):
        square = Square(10, 10, 10, 1)
        square.update(id=7)
        self.assertEqual(square.id, 7)

    def test_create(self):
        square = Square(15, 14, 13, 12)
        r_dictionary = square.to_dictionary()
        second_square = square.create(**r_dictionary)
        self.assertEqual(second_square.id, 12)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file(self):
        square1 = Square(3, 3, 3, 3)
        square2 = Square(4, 4, 4, 4)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            ls = [square1.to_dictionary(), square2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_load_from_file_when_file_doesnt_exist(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
