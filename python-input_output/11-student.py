#!/usr/bin/python3
"""
    Class Student that defines a student by:
        (based on 10-student.py)
        """


class Student:
    """Class to create a student object."""

    def __init__(self, first_name, last_name, age):
        """Initialization for Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of Student attributes."""
        dic = {}
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            for item in attrs:
                if not isinstance(item, str):
                    return self.__dict__
            for key in self.__dict__:
                if key in attrs:
                    dic[key] = self.__dict__[key]
        return dic

    def reload_from_json(self, json):
        """Replaces all attributes of an instance given a json object."""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
