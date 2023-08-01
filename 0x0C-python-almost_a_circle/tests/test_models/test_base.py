#!/usr/bin/python3
"""
Defines unittests for models/base.py.
"""

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


if __name__ == "__main__":
    unittest.main()
