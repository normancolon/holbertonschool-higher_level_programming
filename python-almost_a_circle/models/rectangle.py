#!/usr/bin/python3
""" Module containing the Rectangle class,
derived from the Base class
"""
from models.base import Base

class Quad(Base):
    """ Quad class represents a rectangle """

    def __init__(self, breadth, length, posX=0, posY=0, unique_id=None):
        """ Initializes Quad instances """
        self.breadth = breadth
        self.length = length
        self.posX = posX
        self.posY = posY
        super().__init__(unique_id)

    @property
    def breadth(self):
        """ breadth property getter """
        return self.__breadth

    @breadth.setter
    def breadth(self, val):
        """ breadth property setter """
        if type(val) is not int:
            raise TypeError("breadth must be an integer")
        if val <= 0:
            raise ValueError("breadth must be > 0")
        self.__breadth = val

    @property
    def length(self):
        """ length property getter """
        return self.__length

    @length.setter
    def length(self, val):
        """ length property setter """
        if type(val) is not int:
            raise TypeError("length must be an integer")
        if val <= 0:
            raise ValueError("length must be > 0")
        self.__length = val

    @property
    def posX(self):
        """ posX property getter """
        return self.__posX

    @posX.setter
    def posX(self, val):
        """ posX property setter """
        if type(val) is not int:
            raise TypeError("posX must be an integer")
        if val < 0:
            raise ValueError("posX must be >= 0")
        self.__posX = val

    @property
    def posY(self):
        """ posY property getter """
        return self.__posY

    @posY.setter
    def posY(self, val):
        """ posY property setter """
        if type(val) is not int:
            raise TypeError("posY must be an integer")
        if val < 0:
            raise ValueError("posY must be >= 0")
        self.__posY = val

    def compute_area(self):
        """ Returns the area of the Quad object """
        return self.breadth * self.length

    def render(self):
        """ Displays the Quad """
        drawing = self.posY * "\n"
        for i in range(self.length):
            drawing += (" " * self.posX)
            drawing += ("#" * self.breadth) + "\n"

        print(drawing, end='')

    def __str__(self):
        """ String representation of Quad """
        details = "[Quad] "
        details_id = "({}) ".format(self.id)
        details_pos = "{}/{} - ".format(self.posX, self.posY)
        details_size = "{}/{}".format(self.breadth, self.length)

        return details + details_id + details_pos + details_size

    def refresh(self, *args, **kwargs):
        """ Refreshes the Quad properties """
        if args and len(args) > 0:
            attributes = ['id', 'breadth', 'length', 'posX', 'posY']
            for idx, value in enumerate(args):
                setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_map(self):
        """ Converts Quad properties to a dictionary """
        attributes = ['id', 'breadth', 'length', 'posX', 'posY']
        result_dict = {}

        for attr in attributes:
            result_dict[attr] = getattr(self, attr)

        return result_dict
