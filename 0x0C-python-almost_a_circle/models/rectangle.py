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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of a rectangle.

        Args:
            self: An instance of the Rectangle class.

        Returns:
            The area of the rectangle.

        """
        return self.__width * self.__height

    def display(self):
        """
        Display method to print a rectangle.
        """
        for i in range(self.__height):
            if i == 0:
                for _ in range(self.__y):
                    print("")
            for j in range(self.__width):
                if j == 0:
                    for _ in range(self.__x):
                        print(" ", end='')
                print("#", end='')
            print("")

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
                f" {self.__width}/{self.__height}")

    def update(self, *args):
        """
        Update the attributes of the Rectangle.

        Args:
            *args: Variable number of arguments to update the attributes.
                The arguments should be provided in the following order:
                1. id (int): The new value for the id attribute.
                2. width (int): The new value for the width attribute.
                3. height (int): The new value for the height attribute.
                4. x (int): The new value for the x attribute.
                5. y (int): The new value for the y attribute.
        """
        for i in args:
            if args.index(i) == 0:
                self.id = i
            if args.index(i) == 1:
                self.__width = i
            if args.index(i) == 2:
                self.__height = i
            if args.index(i) == 3:
                self.__x = i
            if args.index(i) == 4:
                self.__y = i
