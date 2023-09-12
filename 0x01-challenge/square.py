#!/usr/bin/python3
"""This module contains the class, Square"""


class Square():
    """This class create square objects"""

    def __init__(self, size=0):
        """instantiate an object"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.height = size
        self.width = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def perimeter_of_my_square(self):
        """returns the perimeter of an object"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """returns the string representation of an object"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(size=2)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
