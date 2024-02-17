#!/usr/bin/python3

class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raise an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value to be an integer and greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
