#!/usr/bin/python3
import unittest
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

