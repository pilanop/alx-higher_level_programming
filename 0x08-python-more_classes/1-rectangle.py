#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle by: (based on `0-rectangle.py`)
"""


class Rectangle:
	"""
	A class representing a rectangle.

	Attributes:
		width (float): The width of the rectangle.
		height (float): The height of the rectangle.

	Methods:
		init__(self, width=0, height=0):
			Initializes a Rectangle object with the given width and height.

		width(self):
			Returns the width of the rectangle.

		width(self, value):
			Sets the width of the Rectangle object.

		height(self):
			Returns the height of the rectangle.

		height(self, value):
			Sets the height of the rectangle.
	"""

	def __init__(self, width=0, height=0):
		"""
		Initializes a Rectangle object with the given width and
		height.

		Args:
			width (float, optional): The width of the rectangle.
			Defaults 0.
			height (float, optional): The height of the rectangle.
			Defaults 0.
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""
		Returns the width of the rectangle.

		Returns:
			The width of the rectangle.
		"""
		return self.__width

	@width.setter
	def width(self, value):
		"""
		Sets the width of the Rectangle object.

		Args:
			value (int): The value to set as the width of
			the Rectangle.

		Raises:
			TypeError: If value is not an integer.
			ValueError: If value is less than 0.

		Returns:
			None
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

		Returns:
			The height of the rectangle.
		"""
		return self.__height

	@height.setter
	def height(self, value):
		"""
		Sets the height of the rectangle.

		Args:
			value (int): The value to set as the height of
			the rectangle.

		Raises:
			TypeError: If value is not an integer.
			ValueError: If value is less than 0.
		"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value
