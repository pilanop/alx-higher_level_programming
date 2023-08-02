#!/usr/bin/python3
"""
Defines unittests for models/square.py.
"""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """
    10. And now, the Square!
    A TestCase for the Square class.
    """

    def setUp(self):
        """
        Set up a new Square instance before each test.
        """
        self.square = Square(5, 1, 2, 3)

    def test_str_method(self):
        """
        Test the `__str__` method.
        """
        self.assertEqual(str(self.square), '[Square] (3) 1/2 - 5')

    def test_instantiation(self):
        """
        Test if the Square instance has been correctly setup.
        """
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)
        self.assertEqual(self.square.id, 3)


class TestSquare_size(unittest.TestCase):
    """
    11. Square size
    A TestCase for the Square class size getter and setter.
    """

    def setUp(self):
        """
        Set up a new Square instance before each test.
        """
        self.square = Square(5, 1, 2, 3)

    def test_getter_setter_size(self):
        """
        Test the size setter and getter.
        """
        self.square.size = 7
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.width, 7)
        self.assertEqual(self.square.height, 7)

    def test_setter_size_type_error(self):
        """
        Test if setting size with an incorrect type raises a TypeError.
        """
        with self.assertRaises(TypeError):
            self.square.size = "not an int"


class TestSquare_update(unittest.TestCase):
    """
    12. Square updates
    A TestCase for the Square class update method.
    """

    def setUp(self):
        """
        Set up a new Square instance before each test.
        """
        self.square = Square(5, 1, 2, 3)

    def test_update_method_with_args(self):
        """
        Test the update method with non-keyword arguments.
        """
        self.square.update(4, 6, 7, 8)
        self.assertEqual(str(self.square), '[Square] (4) 7/8 - 6')

    def test_update_method_with_kwargs(self):
        """
        Test the update method with keyword arguments.
        """
        self.square.update(id=4, size=6, x=7, y=8)
        self.assertEqual(str(self.square), '[Square] (4) 7/8 - 6')


class TestSquare_to_dictionary(unittest.TestCase):
    """
    14. Square instance to dictionary representation
    A TestCase for the Square class to_dictionary method.
    """

    def setUp(self):
        """
        Set up a new Square instance before each test.
        """
        self.square = Square(5, 1, 2, 3)

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary method.
        """
        d = self.square.to_dictionary()
        self.assertEqual(d, {'id': 3, 'size': 5, 'x': 1, 'y': 2})
        self.assertIsInstance(d, dict)


if __name__ == '__main__':
    unittest.main()
