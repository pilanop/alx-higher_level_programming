#!/usr/bin/python3
"""
Defines unittests for models/base.py.
"""
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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


class TestBase_from_json_string(unittest.TestCase):
    """
    17. JSON string to dictionary
    A TestCase for the Base class 'from_json_string' static method.
    """

    def test_from_json_string(self):
        # Test with an actual JSON string
        json_d = '[{"id": 12, "width": 5, "height": 7, "x": 2, "y": 8}]'
        d = Base.from_json_string(json_d)
        self.assertIsInstance(d, list)
        self.assertDictEqual(d[0], {"id": 12, "width": 5, "height": 7, "x": 2,
                                    "y": 8})

    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(Base.from_json_string(""), [])

    def test_None_string(self):
        # Test with None
        self.assertEqual(Base.from_json_string(None), [])

    def test_non_json_string(self):
        # Test with string that's not in JSON format
        with self.assertRaises(ValueError):
            Base.from_json_string('{id: 12, width: 5, height: 7, x: 2, y: 8}')


class TestBase_create(unittest.TestCase):
    """
    18. Dictionary to Instance
    Unittests for testing create method of Base class.
    """

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == '__main__':
    unittest.main()
