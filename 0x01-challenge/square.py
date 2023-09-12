#!/usr/bin/python3
"""This module contains the square class"""


class Square():
    """The square class creates a square object
       Attr:
       width: an integer value >= 0
       height: an integer value >= 0
       __str__(): return a string represent of a square object
       PermiterOfMySquare(): return the perimeter
       area_of_my_square(): return the area
       Assumption:
       Creating a square object defaults to size == 0
       A square can not have unequal sizes
       Instantiating a square object with more than 1 len(args),
       will create an attr, call size == args[0], and ignore
       subsequent elements
       Instantiating a square with one key value pair, defaults to
       creating an illogical square object, hence an exception.
    """

    def __init__(self, width=0, height=0):
        """instatiate a square object"""
        """if args:
            self.width = args[0]
            self.height = args[0]
        else:"""
        """if not kwargs:
            kwargs = {"width":0, "height":0}
        for key, value in kwargs.items():
            setattr(self, key, value)"""
        if width != height:
            raise Exception("width must be == height")
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        """if self.width != self.height:
            raise Exception(" width must be == height")"""
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        """if self.width != self.height:
            raise Exception(" width must be == height")"""
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__width

    def perimeter_of_my_square(self):
        """return the perimeter of a square object"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return string representation of a square object"""
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(3, 3)
    print(s)
    s.width = 4
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
