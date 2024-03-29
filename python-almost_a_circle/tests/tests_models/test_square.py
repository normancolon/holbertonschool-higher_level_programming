#!/usr/bin/python3
import unittest
import os
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        # Ensure no file from previous tests exists
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_creation(self):
        # Test for correct instantiation
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

    def test_square_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_single(self):
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertIn('"size": 1', content)
            self.assertIn('"id": 1', content)

    def test_square_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 0)

    def test_square_load_from_file_exists(self):
        s1 = Square(1)
        Square.save_to_file([s1])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 1)

    # Error handling tests
    def test_of_square_1_exists(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_of_square_1_2_exists(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_of_square_1_2_3_exists(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_of_square_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_of_square_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_of_square_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_of_square_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

if __name__ == "__main__":
    unittest.main()
