#!/usr/bin/python3

class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raise an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
