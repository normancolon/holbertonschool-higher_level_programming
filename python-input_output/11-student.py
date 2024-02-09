#!/usr/bin/python3

"""Defines a class Student with extended functionality."""

class Student:
    """Represents a student with personal details and skills."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with skills.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skills = []  # New attribute to maintain a list of skills

    def to_json(self, attrs=None):
        """Get a selective or full dictionary representation of the Student.

        Parameters:
            attrs (list, optional): The specific attributes to include in the representation.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Update student attributes from a dictionary.

        Parameters:
            json (dict): Attributes and values to update the student with.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def add_skill(self, skill):
        """Add a new skill to the student's skill set.

        Parameters:
            skill (str): A skill to add to the student.
        """
        if skill not in self.skills:
            self.skills.append(skill)

    def remove_skill(self, skill):
        """Remove a skill from the student's skill set, if it exists.

        Parameters:
            skill (str): The skill to remove.
        """
        if skill in self.skills:
            self.skills.remove(skill)
