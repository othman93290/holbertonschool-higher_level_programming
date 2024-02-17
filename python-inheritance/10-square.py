#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with size."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2
