#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square.

    This class inherits from the Rectangle class and adds functionality
    specific to squares.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier of the square.

        """
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """
        Get a formatted string representation of the Square.

        Returns:
            str: A formatted string representation of the Square in the
                following format:
                 "[Square] (id) x/y - size"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Returns the size of the square.

        Returns:
            The size of the square, which is equal to the width.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The value representing the size of the square.

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: Non-keyword arguments that correspond to the attributes
                    of the Square instance. The order of the arguments
                   should be: id, size, x, y.
            **kwargs: Keyword arguments that correspond to the attributes
                    of the Square instance. The available attribute
                      keys are: ["id", "size", "x", "y"].

        """
        if args is not None and len(args) > 0:
            for i in args:
                if args.index(i) == 0:
                    self.id = i
                if args.index(i) == 1:
                    self.size = i
                if args.index(i) == 2:
                    self.x = i
                if args.index(i) == 3:
                    self.y = i
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "y":
                    self.y = value
                if key == "x":
                    self.x = value

    def to_dictionary(self):
        """
        Convert the Square object to a dictionary.

        Returns:
            dict: A dictionary representation of the Square object with the
                  following keys:
                - "id" (int): The unique identifier of the Square.
                - "size" (int): The size of the Square.
                - "x" (int): The x-coordinate
                - "y" (int): The y-coordinate
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

