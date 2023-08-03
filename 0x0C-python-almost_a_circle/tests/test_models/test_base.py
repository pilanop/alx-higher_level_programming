#!/usr/bin/python3
"""
Defines unittests for models/base.py.
"""
import os
import json
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


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


class TestBase_save_to_file(unittest.TestCase):
    """
    16. JSON string to file
    This class is a unit test for the `Base` class 'save_to_file' class method.
    """

    def setUp(self):
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)

    def test_save_to_file(self):
        Base.save_to_file([self.r1, self.r1])

        # Verify the file contents for Rectangle
        if os.path.isfile("Rectangle.json"):
            with open("Rectangle.json", "r") as f:
                content = f.read()
                expected = ('[{"id": 1, "width": 10, "height": 7, "x": 2, '
                            '"y": 8}, {"id": 2, "width": 2, "height": 4, '
                            '"x": 0, "y": 0}]')
                self.assertEqual(json.loads(content), json.loads(expected))

    def tearDown(self):
        """
        Delete generated files after each test
        """
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()