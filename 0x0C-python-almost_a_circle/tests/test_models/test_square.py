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


if __name__ == '__main__':
    unittest.main()
