#!/usr/bin/python3
"""
Defines unittests for models/base.py.
"""

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """
    def setUp(self):
        self.rect1 = Rectangle(5, 6)
        self.rect2 = Rectangle(7, 8, 1, 2, 10)

    def test_width(self):
        self.assertEqual(self.rect1.width, 5)
        self.assertEqual(self.rect2.width, 7)

    def test_height(self):
        self.assertEqual(self.rect1.height, 6)
        self.assertEqual(self.rect2.height, 8)

    def test_x(self):
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect2.x, 1)

    def test_y(self):
        self.assertEqual(self.rect1.y, 0)
        self.assertEqual(self.rect2.y, 2)

    def test_id(self):
        self.assertEqual(self.rect2.id, 10)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
