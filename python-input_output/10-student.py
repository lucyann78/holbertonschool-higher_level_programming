#!/usr/bin/python3
"""
    Class Student that defines a student by:
        (based on 9-student.py)

    Public instance attributes:
        first_name
        last_name
        age

    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):

    Public method def to_json(self, attrs=None): that
    retrieves a dictionary representation of a Student instance
    (same as 10-class_to_json.py):
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
    You are not allowed to import any module.
"""


class Student:
    """ Class to create a dict object """

    def __init__(self, first_name, last_name, age):
        """ Initialization for Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation """
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
