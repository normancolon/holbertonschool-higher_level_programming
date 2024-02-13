#!/usr/bin/python3
"""Module for Base class."""
import json
import os

class Base:
    """A base class for all other classes in the project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        dummy_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        
        with open(filename, "r") as file:
            list_dictionaries = cls.from_json_string(file.read())
            return [cls.create(**dct) for dct in list_dictionaries]
