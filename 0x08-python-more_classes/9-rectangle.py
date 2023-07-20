#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns the string representation of the Rectangle
        with the character #

        Returns:
            str: The string representation of the Rectangle
            with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        new_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += str(self.print_symbol)
            new_str += "\n"

        return new_str[:-1]

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: The string representation of the Rectangle object in the
            format "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        This method is called when the object is being destroyed.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determines which of two rectangles has a bigger or equal area.

        Args:
            rect_1: The first rectangle object.
            rect_2: The second rectangle object.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Args:
            size: An integer specifying the size of the square.

        Returns:
            An instance of the Rectangle class representing a square with
            sides of length 'size'.
        """
        return cls(size, size)
