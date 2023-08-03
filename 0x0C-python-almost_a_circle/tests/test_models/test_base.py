#!/usr/bin/python3
"""
Defines unittests for models/base.py.
"""
import json
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class is a unit test for the `Base` class.
    """

    def setUp(self):
        self.base1 = Base()  # Without explicit id
        self.base2 = Base(15)  # With explicit id

    def test_auto_id(self):
        self.assertEqual(self.base1.id, 1)

    def test_explicit_id(self):
        self.assertEqual(self.base2.id, 15)

    def tearDown(self):
        pass


class TestBase_to_json_string(unittest.TestCase):
    """
    15. Dictionary to JSON string
    A TestCase for the Base class 'to_json_string' static method.
    """

    def test_to_json_string(self):
        # Test with an actual list of dictionaries
        d = [{"id": 12, "width": 5, "height": 7, "x": 2, "y": 8}]
        json_d = Base.to_json_string(d)
        self.assertIsInstance(json_d, str)
        self.assertDictEqual(json.loads(json_d)[0], d[0])

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_None_list(self):
        # Test with None
        self.assertEqual(Base.to_json_string(None), "[]")


if __name__ == '__main__':
    unittest.main()