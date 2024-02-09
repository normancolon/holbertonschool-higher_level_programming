#!/usr/bin/python3

"""Defines a class Learner for representing participants of online courses."""

class Learner:
    """Represents an individual enrolled in online courses."""

    def __init__(self, first_name, last_name, age, enrolled_courses=None):
        """Initializes a new Learner instance.

        Parameters:
            first_name (str): The learner's first name.
            last_name (str): The learner's last name.
            age (int): The learner's age.
            enrolled_courses (list): A list of courses the learner is enrolled in.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.enrolled_courses = enrolled_courses if enrolled_courses is not None else []

    def add_course(self, course_name):
        """Adds a new course to the learner's list of enrolled courses.

        Parameters:
            course_name (str): The name of the course to add.
        """
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)

    def profile_summary(self):
        """Generates a summary of the learner's profile.

        Returns:
            dict: A dictionary containing the learner's details and enrolled courses.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "enrolled_courses": self.enrolled_courses
        }

