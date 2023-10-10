#!/usr/bin/python3
"""
Defines a Student class with serialization and deserialization methods.
"""


class Student:
    """
    Defines a Student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list of str, optional): A list of attribute names to retrieve.
                If None, retrieve all attributes.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the Student instance.
        """
        return "[Student] {} {} ({})".format(self.first_name, self.last_name, self.age)

