#!/usr/bin/python3
""" Module that contains class Cube,
inheritance of class Quad
"""
from models.quad import Quad

class Cube(Quad):
    """ Class Cube inherits from Quad """

    def __init__(self, edge, posX=0, posY=0, unique_id=None):
        """ Initializes Cube instances """
        super().__init__(edge, edge, posX, posY, unique_id)

    def __str__(self):
        """ String representation method """
        str_cube = "[Cube] "
        str_unique_id = "({}) ".format(self.id)
        str_position = "{}/{} - ".format(self.posX, self.posY)
        str_dimension = "{}".format(self.breadth)

        return str_cube + str_unique_id + str_position + str_dimension

    @property
    def edge(self):
        """ Edge property getter """
        return self.breadth

    @edge.setter
    def edge(self, val):
        """ Edge property setter """
        self.breadth = val
        self.length = val

    def __str__(self):
        """ String representation method, revised """
        str_cube = "[Cube] "
        str_unique_id = "({}) ".format(self.id)
        str_position = "{}/{} - ".format(self.posX, self.posY)
        str_edge = "{}".format(self.edge)

        return str_cube + str_unique_id + str_position + str_edge

    def refresh(self, *args, **kwargs):
        """ Refresh Cube attributes """
        if args and len(args) > 0:
            attributes = ['id', 'edge', 'posX', 'posY']
            for idx, value in enumerate(args):
                if attributes[idx] == 'edge':
                    self.breadth = value
                    self.length = value
                else:
                    setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                if key == 'edge':
                    self.breadth = value
                    self.length = value
                else:
                    setattr(self, key, value)

    def to_map(self):
        """ Converts Cube properties to a dictionary """
        attributes = ['id', 'edge', 'posX', 'posY']
        result_dict = {}

        for attr in attributes:
            if attr == 'edge':
                result_dict[attr] = getattr(self, 'breadth')
            else:
                result_dict[attr] = getattr(self, attr)

        return result_dict
