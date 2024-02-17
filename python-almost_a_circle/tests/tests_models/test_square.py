#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """Test the creation of a Square."""
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

    def test_square_string_representation(self):
        """Test the string representation of a Square."""
        s1 = Square(4, 1, 2, 10)
        self.assertEqual(str(s1), "[Square] (10) 1/2 - 4")

    def test_square_to_dictionary(self):
        """Test converting a Square to a dictionary."""
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected)

    def test_square_update_args(self):
        """Test updating Square properties using *args."""
        s1 = Square(5, 0, 0, 1)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_square_update_kwargs(self):
        """Test updating Square properties using **kwargs."""
        s1 = Square(5, 0, 0, 1)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    # Additional tests for error handling
    def test_square_with_string_size(self):
        """Test of Square("1") exists"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_with_string_x(self):
        """Test of Square(1, "2") exists"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_with_string_y(self):
        """Test of Square(1, 2, "3") exists"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_valid_arguments(self):
        """Test of Square(1, 2, 3, 4) exists"""
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_square_with_negative_size(self):
        """Test of Square(-1) exists"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_with_negative_x(self):
        """Test of Square(1, -2) exists"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_with_negative_y(self):
        """Test of Square(1, 2, -3) exists"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_with_zero_size(self):
        """Test of Square(0) exists"""
        with self.assertRaises(ValueError):
            Square(0)

if __name__ == "__main__":
    unittest.main()
