#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class represents a rectangle and is a subclass of the Base
    class. It has properties for width, height, x-coordinate, and y-coordinate.

    Methods:
        width.setter: Sets the width of the rectangle.
        height.setter: Sets the height of the rectangle.
        x.setter: Sets the x-coordinate of the rectangle.
        y.setter: Sets the y-coordinate of the rectangle.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value: The value to set as the width.

        """
        self.__width = value

    @property
    def height(self):
        """

        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value to set.

        """
        self.__height = value

    @property
    def x(self):
        """
        This method is a getter for the 'x' attribute of the Rectangle class.

        Returns:
            int: The value of the 'x' attribute.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the value of x for the Rectangle object.

        Args:
            value: The value to set as the x-coordinate of the Rectangle.

        """
        self.__x = value

    @property
    def y(self):
        """
        This method is a getter for the "y" attribute of the Rectangle class.

        Returns:
            int: The value of the "y" attribute.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of 'y' for the Rectangle object.

        Args:
            value: The value to set for 'y'.

        """
        self.__y = value
