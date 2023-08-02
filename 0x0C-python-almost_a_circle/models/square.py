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
