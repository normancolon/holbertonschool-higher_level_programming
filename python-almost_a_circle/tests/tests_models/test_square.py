#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
import os

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        # Ensure no file from previous tests exists
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_creation(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.id, 1)

        s2 = Square(3, 2)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.id, 2)

        s3 = Square(4, 1, 3, 89)
        self.assertEqual(s3.size, 4)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 89)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 4)

    def test_square_string_representation(self):
        s1 = Square(4, 1, 2, 10)
        self.assertEqual(str(s1), "[Square] (10) 1/2 - 4")

    def test_square_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected)

    def test_square_update_args(self):
        s1 = Square(5, 0, 0, 1)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        # Test various forms of update with args
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(89, 1)
        self.assertEqual(s1.size, 1)
        s1.update(89, 1, 2)
        self.assertEqual(s1.x, 2)
        s1.update(89, 1, 2, 3)
        self.assertEqual(s1.y, 3)

    def test_square_update_kwargs(self):
        s1 = Square(5, 0, 0, 1)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

        # Test various forms of update with kwargs
        s1.update(id=89)
        self.assertEqual(s1.id, 89)
        s1.update(id=89, size=1)
        self.assertEqual(s1.size, 1)
        s1.update(id=89, size=1, x=2)
        self.assertEqual(s1.x, 2)
        s1.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s1.y, 3)

    def test_square_create(self):
        s1_dict = {'id': 89, 'size': 30, 'x': 4, 'y': 2}
        s1 = Square.create(**s1_dict)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 30)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 2)
        self.assertTrue(isinstance(s1, Square))

        # Test creation with various dictionary configurations
        s2 = Square.create(**{'id': 89})
        self.assertEqual(s2.id, 89)
        s3 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s3.size, 1)
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s4.x, 2)
        s5 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s5.y, 3)

    def test_square_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test saving a list with one Square
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertTrue(len(content) > 2)  # Checks if the file is not empty

    def test_square_load_from_file(self):
        # Test loading when file does not exist
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 0)

        # Test loading when file exists
        s1 = Square(1)
        Square.save_to_file([s1])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)

    def test_square_errors(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

if __name__ == "__main__":
    unittest.main()
