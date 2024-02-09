#!/usr/bin/python3

"""Defines a class Student for representing student details and course enrollments."""

class Student:
    """Represents a student's basic information and courses they're enrolled in."""

    def __init__(self, first_name, last_name, age, courses=None):
        """Initializes a new Student.

        Parameters:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
            courses (list): Optional. A list of courses the student is enrolled in.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = courses if courses is not None else []

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student.

        If attrs is specified, only attributes named in attrs are included.

        Parameters:
            attrs (list): Optional. Specifies which attributes to include in the dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def update_attributes(self, **kwargs):
        """Updates the student's attributes with provided keyword arguments.

        Parameters:
            **kwargs: Arbitrary keyword arguments representing attributes and their values.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def enroll_in_course(self, course_name):
        """Adds a new course to the student's list of enrolled courses.

        Parameters:
            course_name (str): The name of the course to enroll in.
        """
        if course_name not in self.courses:
            self.courses.append(course_name)

