#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_auto_id(self):
        """Test automatic ID assignment."""
        Base._Base__nb_objects = 0
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

# New test class for Rectangle
class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
   
    def test_rectangle(self):
        """Test case for non-list arguments"""
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
        """Test case for negative arguments"""
        self.assertRaises(ValueError, Rectangle, 10, -2)
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(ValueError, Rectangle, 10, 2, -3)
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -4)

    def test_rectangle_with_zero_arguments(self):
        """Test case for zero arguments"""
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_rectangle_with_non_list_argument(self):
        """Test case for non-list arguments"""
        self.assertRaises(TypeError, Rectangle, 2, "10")
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 10, 2, "5")
        self.assertRaises(TypeError, Rectangle, 10, 2, 5, "3")

    def test_area(self):
        """Test case for area method"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    def test_str_rectangle(self):
        """Test case for __str__ method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """Test of display() exists"""
        r1 = Rectangle(4, 2, 1, 1)
        expected_output = "\n ####\n ####\n"
        with patch('sys.stdout', new_callable=StringIO) as mocked_output:
            r1.display()
            self.assertEqual(mocked_output.getvalue(), expected_output)

    def test_display_without_x_and_y(self):
        """Test case for display method without x and y"""
        r1 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new_callable=StringIO) as mocked_output:
            r1.display()
            self.assertEqual(mocked_output.getvalue(), expected_output)

 # New test methods based on the additional requirements
    def test_to_dictionary(self):
        """Test of to_dictionary() in Rectangle exists"""
        r1 = Rectangle(10, 7, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'id': 9, 'width': 10, 'height': 7, 'x': 2, 'y': 1})

    def test_update(self):
        """Test of update() in Rectangle exists"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), '[Rectangle] (10) 10/10 - 10/10')

    # Test update with kwargs
    def test_update_kwargs(self):
        """Test of update with kwargs in Rectangle"""
        r1 = Rectangle(5, 5, 5, 5, 5)
        r1.update(id=89)
        self.assertEqual(r1.id, 89)
        r1.update(width=1)
        self.assertEqual(r1.width, 1)
        
if __name__ == '__main__':
    unittest.main()
