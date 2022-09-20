#!/usr/bin/python3
"""rectangle full implementation"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiate an objet with width and height"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set object width to value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set object height to value"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
