#!/usr/bin/python3
"""Module for CountedIterator class"""


class CountedIterator:
    """The CountedIterator class that counts iterations over an iterable."""

    def __init__(self, iterable):
        """Initialization with an iterable."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Overrid next method return the next item increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the count of items iterated."""
        return self.counter
