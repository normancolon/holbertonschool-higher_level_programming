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

    def test_square_create(self):
        """Test the create method of a Square."""
        s1_dict = {'id': 89, 'size': 30, 'x': 4, 'y': 2}
        s1 = Square.create(**s1_dict)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 30)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 2)
        self.assertTrue(isinstance(s1, Square))

    def test_square_save_to_file_none(self):
        """Test saving to file with None."""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_empty(self):
        """Test saving to file with an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_load_from_file_no_file(self):
        """Test loading Squares from a file that doesn't exist."""
        try:
            squares = Square.load_from_file()
            self.assertEqual(len(squares), 0)
        except Exception as e:
            self.fail(f"Unexpected exception thrown: {e}")

    # Additional tests for Square functionality...

if __name__ == "__main__":
    unittest.main()
