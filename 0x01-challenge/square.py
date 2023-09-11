#!/usr/bin/python3
"""This module contains the square class"""


class square(object):
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

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """instatiate a square object"""
        if args:
            self.size = args[0]
            self.width = self.__size
            self.height = self.__size
        else:
            for key, value in kwargs.items():
                if type(value) is not int:
                    raise TypeError(key + " must be an integer")
                if value < 0:
                    raise ValueError(key + " must be >= 0")
                setattr(self, key, value)
            if self.width != self.height:
                raise Exception(" width must be == height")

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """return the perimeter of a square object"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """return string representation of a square object"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
