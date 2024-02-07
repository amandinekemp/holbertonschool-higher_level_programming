#!/usr/bin/python3
"""Module defining a Square class"""

class Square:
    """Square class representing a geometric square with a size attribute"""

    def __init__(self, size=0):
        """
        Initializes a square instance with an optional size
        
        Args:
            size (int, optional): The size of the square. Default is 0
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute
        
        Return:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute

        Args:
            value (int): The new size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square

        Return:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character to stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
