#!/usr/bin/python3
"""
defines a class Student that defines a student
"""


class Student:
    """
    Class Student

    Represents a student with a first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object with the given first name,
        last name, and age.

        Args:
            first_name: A string representing the first name of the student.
            last_name: A string representing the last name of the student.
            age: An integer representing the age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convert the Student object to a JSON serializable dictionary.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        return self.__dict__
