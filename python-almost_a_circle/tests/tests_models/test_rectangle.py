import unittest
from models.base import Base
from models.rectangle import Rectangle
# from models.square import Square  # Uncomment if Square tests are added later

class TestBase(unittest.TestCase):
    # Existing TestBase methods...

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

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
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -4)

    def test_rectangle_with_zero_arguments(self):
        """Test case for zero arguments"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_rectangle_with_non_int_argument(self):
        """Test case for non-integer arguments"""
        with self.assertRaises(TypeError):
            Rectangle(2, "10")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "5")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, "3")

    def test_area(self):
        """Test the area method of the Rectangle class."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    def test_str_rectangle(self):
        """Test the __str__ method of Rectangle."""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

# Additional tests for Rectangle can be added here

if __name__ == "__main__":
    unittest.main()
