#!/usr/bin/python3
class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

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
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of strings representing names of attributes to include.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those in the provided JSON dictionary.

        Args:
            json (dict): A dictionary with attributes to update on the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)

# The script below is to demonstrate using the `Student` class and its new `reload_from_json` method.
if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    print("Before:")
    print(vars(student_1))

    # Simulating loading student data from JSON
    json_data = {'first_name': 'Jane', 'last_name': 'Doe', 'age': 30}
    student_1.reload_from_json(json_data)
    print("\nAfter:")
    print(vars(student_1))
