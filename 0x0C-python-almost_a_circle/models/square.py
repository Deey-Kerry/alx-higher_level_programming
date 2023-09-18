#!/usr/bin/python3
"""the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from class Rectangle and its attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints string size"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """sets attributes and arguements"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary rep"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d