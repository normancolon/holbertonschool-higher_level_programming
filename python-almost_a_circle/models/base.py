#!/usr/bin/python3
""" Module for Base class definition """
import json
import csv
import os

class Base:
    """ Base class """
    __id_counter = 0

    def __init__(self, id=None):
        """ Initialization of instances """
        if id is not None:
            self.id = id
        else:
            Base.__id_counter += 1
            self.id = Base.__id_counter

    @staticmethod
    def to_json_string(list_of_dicts):
        """ Converts list of dictionaries to JSON string """
        if list_of_dicts is None or list_of_dicts == "[]":
            return "[]"
        return json.dumps(list_of_dicts)

    @classmethod
    def save_to_json_file(cls, objects_list):
        """ Saves object to a JSON file """
        file_name = "{}.json".format(cls.__name__)
        dictionaries_list = []

        if objects_list:
            for obj in objects_list:
                dictionaries_list.append(obj.to_dictionary())
        json_string = cls.to_json_string(dictionaries_list)

        with open(file_name, 'w') as json_file:
            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_str):
        """ Converts JSON string to dictionary """
        if not json_str:
            return []
        return json.loads(json_str)

    @classmethod
    def instantiate(cls, **attributes):
        """ Instantiates an object """
        if cls.__name__ == "Rectangle":
            new_instance = cls(10, 10)
        else:
            new_instance = cls(10)
        new_instance.update(**attributes)
        return new_instance

    @classmethod
    def load_from_json_file(cls):
        """ Loads list of instances from JSON file """
        file_path = "{}.json".format(cls.__name__)

        if not os.path.isfile(file_path):
            return []

        with open(file_path, 'r') as json_file:
            objects_str = json_file.read()

        objects_dicts = cls.from_json_string(objects_str)
        instances = [cls.instantiate(**dict_obj) for dict_obj in objects_dicts]

        return instances

    @classmethod
    def save_to_csv_file(cls, instances_list):
        """ Saves instances to a CSV file """
        file_name = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            default_values = [0, 0, 0, 0, 0]
            columns = ['id', 'width', 'height', 'x', 'y']
        else:
            default_values = ['0', '0', '0', '0']
            columns = ['id', 'size', 'x', 'y']

        rows = []

        if instances_list:
            for instance in instances_list:
                row = [instance.to_dictionary()[col] for col in columns]
                rows.append(row)

        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(rows)

    @classmethod
    def load_from_csv_file(cls):
        """ Loads instances from a CSV file """
        file_name = "{}.csv".format(cls.__name__)

        if not os.path.exists(file_name):
            return []

        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)

        if cls.__name__ == "Rectangle":
            keys = ['id', 'width', 'height', 'x', 'y']
        else:
            keys = ['id', 'size', 'x', 'y']

        objects_attrs = [{keys[i]: int(val) for i, val in enumerate(row)} for row in rows]
        instances = [cls.instantiate(**attrs) for attrs in objects_attrs]

        return instances
