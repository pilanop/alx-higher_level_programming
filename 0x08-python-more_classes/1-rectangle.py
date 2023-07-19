#!/usr/bin/python3

"""A class Rectangle that defines a rectangle (based on 0-rectangle.py)
"""


class Rectangle:
	"""
	A class representing a rectangle.

	Attributes:
		width (int): The width of the rectangle.
		height (int): The height of the rectangle.
	"""

	def __init__(self, width=0, height=0):
		"""
		Initializes a Rectangle object with the given width and height.

		Args:
			width (int, optional): The width of the Rectangle.
			Defaults to 0.
			height (int, optional): The height of the Rectangle.
			Defaults to 0.

		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""
		Returns the width of the rectangle.
		"""
		return self.__width

	@width.setter
	def width(self, value):
		"""
		Sets the width of the Rectangle object.

		Raises:
			TypeError: If value is not an integer.
			ValueError: If value is less than 0.
		"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""
		Returns the height of the rectangle.
		"""
		return self.__height

	@height.setter
	def height(self, value):
		"""
		Sets the height of the rectangle.

		Raises:
			TypeError: If value is not an integer.
			ValueError: If value is less than 0.
		"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value
