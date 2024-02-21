#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
	"""Defines a Rectangle class."""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""Initializes the restangle.

		 Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle. Defaults to 0.
            y (int): The y coordinate of the rectangle. Defaults to 0.
            id (int): The id of the rectangle. Defaults to None.
        """
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		"""Gets the width of the rectangle."""
		return self.__width
	
	@width.setter
	def width(self, value):
		"""Sets the width of the rectangle."""
		self.__width = value
	
	@property
	def height(self):
		"""Gets the height of the rectangle."""
		return self.__height
	
	@height.setter
	def height(self, value):
		"""Sets the height of the rectangle."""
		self.__height = value
	
	@property
	def x(self):
		"""Gets the x coordinate of the rectangle."""
		return self.__x
	
	@x.setter
	def x(self, value):
		"""Sets the x coordinate of the rectangle."""
		self.__x = value

	@property
	def y(self):
		"""Gets the y coordinate of the rectangle."""
		return self.__y
	
	@y.setter
	def y(self, value):
		"""Sets the y coordinate of the rectangle."""
		self.__y = value
