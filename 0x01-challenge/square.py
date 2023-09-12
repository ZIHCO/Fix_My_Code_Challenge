#!/usr/bin/python3
"""This module contains the class, Square"""


class Square():
    """This class create square objects"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """instantiate an object"""
        for key, value in kwargs.items():
            setattr(self, key, value)

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

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
