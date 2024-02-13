#!/usr/bin/python3
"""Module to test the Square class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class SquareTestSuite(unittest.TestCase):
    """Defines a suite of tests for the Square class behavior."""

    def setUp(self):
        """Method called to prepare the test fixture."""
        Base._Base__nb_objects = 0

    def test_create_square(self):
        """Tests square creation with default attributes."""
        square_default = Square(3)
        self.assertEqual(square_default.size, 3)
        self.assertEqual(square_default.width, 3)
        self.assertEqual(square_default.height, 3)
        self.assertEqual(square_default.x, 0)
        self.assertEqual(square_default.y, 0)
        self.assertEqual(square_default.id, 1)

    def test_square_custom_attributes(self):
        """Tests square creation with custom attributes."""
        square_custom = Square(2, 5, 5, 4)
        self.assertEqual(square_custom.size, 2)
        self.assertEqual(square_custom.x, 5)
        self.assertEqual(square_custom.y, 5)
        self.assertEqual(square_custom.id, 4)

    def test_multiple_square_instances(self):
        """Tests creation of multiple square instances to ensure uniqueness."""
        first_square = Square(1, 1)
        second_square = Square(1, 1)
        self.assertNotEqual(first_square, second_square)
        self.assertNotEqual(first_square.id, second_square.id)

    def test_square_base_instance(self):
        """Tests if a Square is an instance of Base."""
        square_instance = Square(1)
        self.assertIsInstance(square_instance, Base)

    def test_square_rectangle_instance(self):
        """Tests if a Square is an instance of Rectangle."""
        square_instance = Square(1)
        self.assertIsInstance(square_instance, Rectangle)

    def test_no_args_to_square(self):
        """Tests error raised when no arguments are passed to Square."""
        with self.assertRaises(TypeError):
            Square()

    def test_excess_arguments_to_square(self):
        """Tests error raised when too many arguments are passed to Square."""
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1)

    def test_private_attribute_access(self):
        """Tests AttributeError when accessing private attributes directly."""
        square_instance = Square(1)
        with self.assertRaises(AttributeError):
            print(square_instance.__width)
        with self.assertRaises(AttributeError):
            print(square_instance.__height)
        with self.assertRaises(AttributeError):
            print(square_instance.__x)
        with self.assertRaises(AttributeError):
            print(square_instance.__y)

    def test_invalid_attribute_types(self):
        """Tests TypeError when passing incorrect types to Square attributes."""
        with self.assertRaises(TypeError):
            Square("3")
        with self.assertRaises(TypeError):
            Square(2, "5")
        with self.assertRaises(TypeError):
            Square(2, 2, "5")

    def test_invalid_attribute_values(self):
        """Tests ValueError when passing invalid values to Square attributes."""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(2, -2)
        with self.assertRaises(ValueError):
            Square(3, 3, -3)

    def test_square_area(self):
        """Tests correct area calculation for a Square."""
        square_instance = Square(4)
        self.assertEqual(square_instance.area(), 16)
        square_instance.size = 5
        self.assertEqual(square_instance.area(), 25)

    def test_square_display(self):
        """Tests the stdout display output of a Square."""
        square_instance = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square_instance.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_square_str(self):
        """Tests the custom string representation of a Square."""
        square_instance = Square(4, 2, 2, 1)
        expected_str = "[Square] (1) 2/2 - 4\n"
        self.assertEqual(square_instance.__str__(), expected_str)

    def test_square_update(self):
        """Tests the update method for a Square."""
        square_instance = Square(1, 1, 1, 1)
        square_instance.update(10, 2, 3, 4)
        self.assertEqual(square_instance.id, 10)
        self.assertEqual(square_instance.size, 2)
        self.assertEqual(square_instance.x, 3)
        self.assertEqual(square_instance.y, 4)

    def test_square_to_dictionary(self):
        """Tests the dictionary representation of a Square."""
        square_instance = Square(1, 2, 3, 4)
        square_dict = square_instance.to_dictionary()
        self.assertIsInstance(square_dict, dict)
        expected_keys = ["id", "size", "x", "y"]
        self.assertTrue(all(key in square_dict for key in expected_keys))

    def test_square_json_serialization(self):
        """Tests JSON string serialization of a Square."""
        square_instance = Square(2)
        square_dict = square_instance.to_dictionary()
        json_str = Base.to_json_string([square_dict])
        self.assertIsInstance(json_str, str)
        self.assertListEqual(json.loads(json_str), [square_dict])

    def test_square_file_storage(self):
        """Tests saving and loading Square instances from a file."""
        square_instance = Square(5)
        Square.save_to_file([square_instance])
        loaded_squares = Square.load_from_file()
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertEqual(loaded_squares[0].size, 5)

if __name__ == "__main__":
    unittest.main()
