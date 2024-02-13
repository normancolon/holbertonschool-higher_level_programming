#!/usr/bin/python3
import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle

class CheckBaseDocs(unittest.TestCase):
    """Verification for documentation"""
    def test_module_documentation(self):
        """Validate module has documentation"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_documentation(self):
        """Ensure class is documented"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_documentation(self):
        """Ensure methods have documentation"""
        for method in dir(Base):
            self.assertTrue(len(method.__doc__) > 0)

class CheckBasePep8(unittest.TestCase):
    """PEP8 compliance check"""
    def test_pep8_conformance(self):
        """Check PEP8 for base.py"""
        import pep8
        pep_checker = pep8.StyleGuide(quiet=True)
        base_file = 'models/base.py'
        test_base_file = 'tests/test_models/test_base.py'
        pep_result = pep_checker.check_files([base_file, test_base_file])
        self.assertEqual(pep_result.total_errors, 0, "PEP8 issues found.")

class ValidateBase(unittest.TestCase):
    """Validation tests for Base class"""
    @classmethod
    def setUp(cls):
        """Setup test context"""
        Base._Base__nb_objects = 0
        cls.obj1 = Base()
        cls.obj2 = Base()
        cls.obj3 = Base(98)
        cls.obj4 = Base()
        cls.obj5 = Base("string")
        cls.obj6 = Base(7.7)
        cls.rect1 = Rectangle(1, 1)

    def test_identity(self):
        """ID attribute tests"""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 98)
        self.assertEqual(self.obj4.id, 3)
        self.assertEqual(self.obj5.id, "string")
        self.assertEqual(self.obj6.id, 7.7)

    def test_json_conversion(self):
        """JSON string conversion test"""
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        dict1 = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        json_conversion = Base.to_json_string(dict1)
        self.assertTrue(isinstance(json_conversion, str))
        converted_dict = json.loads(json_conversion)
        self.assertEqual(converted_dict, dict1)

    def test_json_to_dict(self):
        """JSON string to dictionary conversion test"""
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string(None), [])

    @classmethod
    def tearDown(cls):
        """Cleanup test context"""
        pass
