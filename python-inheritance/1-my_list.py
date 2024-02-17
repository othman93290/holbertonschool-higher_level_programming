#!/usr/bin/python3

class MyList(list):
    """A subclass of list."""

    def print_sorted(self):
        """Print the list sorted."""
        print(sorted(self))
