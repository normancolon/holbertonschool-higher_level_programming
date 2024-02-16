#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_manual_id(self):
        """Test manual ID assignment."""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_none(self):
        """Test JSON string conversion with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test JSON string conversion with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dict(self):
        """Test JSON string conversion with list of dictionaries."""
        dict_list = [{'id': 12}]
        self.assertEqual(Base.to_json_string(dict_list), '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test loading from JSON string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """Test loading from JSON string with empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_with_data(self):
        """Test loading from JSON string with valid JSON string."""
        json_str = '[{"id": 89}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 89}])

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """Test creation of Rectangle with various arguments."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_rectangle_with_negative_arguments(self):
        """Test Rectangle creation with negative arguments."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -4)

    def test_rectangle_with_zero_arguments(self):
        """Test Rectangle creation with zero arguments."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_rectangle_with_non_int_argument(self):
        """Test Rectangle creation with non-integer arguments."""
        with self.assertRaises(TypeError):
            Rectangle(2, "10")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "5")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, "3")

    def test_area(self):
        """Test the area method of Rectangle."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    def test_str_rectangle(self):
        """Test the __str__ method of Rectangle."""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

if __name__ == "__main__":
    unittest.main() 
