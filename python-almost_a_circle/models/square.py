#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class that inherits from Rectangle."""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square, affecting both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
