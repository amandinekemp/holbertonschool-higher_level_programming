#!/usr/bin/python3

"""Module defining a Square class"""


class Square:
    """
    Class representing a square with size and position attributes

    Attributes:
        size (int): Size of one side of the square
        position (tuple): Position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance with size and position

        Args:
            size (int, optional): The size of the square. Defaults to 0
            position (tuple, optional): The position of the square
            Defaults to (0, 0)
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for the size attribute

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute

        Returns:
            tuple: The position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute

        Args:
            value (tuple): The new position of the square

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square with the character '#' to stdout
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
