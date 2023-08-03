#!/usr/bin/python3
"""
Defines unittests for models/rectangle.py.
"""
from io import StringIO
import sys
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


class TestRectangle_Validate_Attributes(unittest.TestCase):
    """
    3. Validate attributes
    This class contains unit tests for validating the attributes of the
    Rectangle class.
    """

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("not a number", 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "not a number")
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, "not a number")
        with self.assertRaises(ValueError):
            Rectangle(5, 6, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 0, "not a number")
        with self.assertRaises(ValueError):
            Rectangle(5, 6, 0, -1)


class TestRectangle_Area_First(unittest.TestCase):
    """
    4. Area-first
    Unit tests for the `TestRectangle_Area_First` class.
    """

    def setUp(self):
        self.rect1 = Rectangle(5, 6)
        self.rect2 = Rectangle(7, 8, 1, 2, 10)

    def test_area(self):
        self.assertEqual(self.rect1.area(), 30)  # Area = width*height
        self.assertEqual(self.rect2.area(), 56)  # Area = width*height

    def tearDown(self):
        pass


class TestRectangle_Display0(unittest.TestCase):
    """
    5. Display #0
    Unit test for the `display` method in the `Rectangle` class.
    """

    def setUp(self):
        self.rect1 = Rectangle(3, 2)
        self.rect2 = Rectangle(6, 4)
        self.saved_stdout = sys.stdout

    def test_display(self):
        out = StringIO()
        sys.stdout = out
        self.rect1.display()
        output = out.getvalue().strip()
        expected_output = "###\n###"
        self.assertEqual(output, expected_output)

    def test_display2(self):
        out = StringIO()
        sys.stdout = out
        self.rect2.display()
        output = out.getvalue().strip()
        expected_output = "######\n######\n######\n######"
        self.assertEqual(output, expected_output)

    def tearDown(self):
        sys.stdout = self.saved_stdout


class TestRectangle_Str(unittest.TestCase):
    """
    6. __str__
    Unit test for the `__str__` method in the `Rectangle` class.
    """

    def setUp(self):
        self.rect1 = Rectangle(5, 6)
        self.rect2 = Rectangle(7, 8, 1, 2, 10)

    def test_str1(self):
        self.assertEqual(str(self.rect2), "[Rectangle] (10) 1/2 - 7/8")

    def tearDown(self):
        pass


class TestRectangle_Display1(unittest.TestCase):
    """
    7. Display #1
    Unit test for the `display` method in the `Rectangle` class.
    """
    def setUp(self):
        self.rect1 = Rectangle(3, 2, 1, 2)
        self.rect2 = Rectangle(2, 2, 0, 1)
        self.rect3 = Rectangle(2, 4, 3, 2)
        self.saved_stdout = sys.stdout

    def test_display(self):
        out = StringIO()
        sys.stdout = out
        self.rect1.display()
        output = out.getvalue()
        expected_output = "\n\n ###\n ###\n"
        self.assertEqual(output, expected_output)

    def test_display2(self):
        out = StringIO()
        sys.stdout = out
        self.rect2.display()
        output = out.getvalue()
        expected_output = "\n##\n##\n"
        self.assertEqual(output, expected_output)

    def test_display3(self):
        out = StringIO()
        sys.stdout = out
        self.rect3.display()
        output = out.getvalue()
        expected_output = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(output, expected_output)

    def tearDown(self):
        sys.stdout = self.saved_stdout


class TestRectangle_Update0(unittest.TestCase):
    """
    8. Update #0
    Unit test for the `update` method in the `Rectangle` class.
    """

    def setUp(self):
        self.rect1 = Rectangle(5, 6)
        self.rect2 = Rectangle(7, 8, 1, 2, 10)

    def test_update(self):
        # Update some attributes
        self.rect1.update(89, 2, 3)
        self.assertEqual(self.rect1.id, 89)
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.height, 3)

        # Update all attributes
        self.rect2.update(99, 2, 3, 4, 5)
        self.assertEqual(self.rect2.id, 99)
        self.assertEqual(self.rect2.width, 2)
        self.assertEqual(self.rect2.height, 3)
        self.assertEqual(self.rect2.x, 4)
        self.assertEqual(self.rect2.y, 5)

    def test_update_no_args(self):
        original_id = self.rect1.id
        original_width = self.rect1.width
        original_height = self.rect1.height
        original_x = self.rect1.x
        original_y = self.rect1.y

        self.rect1.update()

        self.assertEqual(self.rect1.id, original_id)
        self.assertEqual(self.rect1.width, original_width)
        self.assertEqual(self.rect1.height, original_height)
        self.assertEqual(self.rect1.x, original_x)
        self.assertEqual(self.rect1.y, original_y)

    def tearDown(self):
        pass


class TestRectangle_Update_Kwargs(unittest.TestCase):
    """
    9. Update #1
    Unit test for the kwargs functionality of the `update` method
    in the `Rectangle` class.
    """

    def setUp(self):
        self.rec1 = Rectangle(10, 11)
        self.rect2 = Rectangle(12, 13, 4, 3, 50)

    def test_update_some_kwargs(self):
        # Update some attributes
        self.rec1.update(id=90, width=3, height=2)
        self.assertEqual(self.rec1.id, 90)
        self.assertEqual(self.rec1.width, 3)
        self.assertEqual(self.rec1.height, 2)

    def test_update_all_kwargs(self):
        # Update all attributes
        self.rect2.update(id=100, width=4, height=5, x=3, y=2)
        self.assertEqual(self.rect2.id, 100)
        self.assertEqual(self.rect2.width, 4)
        self.assertEqual(self.rect2.height, 5)
        self.assertEqual(self.rect2.x, 3)
        self.assertEqual(self.rect2.y, 2)

    def test_update_args_kwargs(self):
        # Update using both args and kwargs; args should have precedence
        self.rec1.update(90, 20, 30, id=80, width=3, height=2)

        # Only the values passed in args should have updated
        self.assertEqual(self.rec1.id, 90)
        self.assertEqual(self.rec1.width, 20)
        self.assertEqual(self.rec1.height, 30)
        # x and y should remain the initial values as they were not updated
        # through args
        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec1.y, 0)

    def tearDown(self):
        pass


class TestRectangle_to_dictionary(unittest.TestCase):
    """
    13. Rectangle instance to dictionary representation
    Tests for the to_dictionary method of the Rectangle class.
    """

    def setUp(self):
        """
        Set up for the tests.
        """
        self.rectangle = Rectangle(10, 15, 20, 25, 30)

    def test_to_dictionary_output(self):
        """
        Test the output of the to_dictionary method.
        """
        expected_output = dict(id=30, width=10, height=15, x=20, y=25)
        self.assertEqual(self.rectangle.to_dictionary(), expected_output)


if __name__ == "__main__":
    unittest.main()
