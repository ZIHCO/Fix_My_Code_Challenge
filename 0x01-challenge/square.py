#!/usr/bin/python3
"""This module contains the class, Square"""


class Square():
    """This class create square objects"""

    width = 0
    height = 0

    def __init__(self, **kwargs):
        """instantiate an object"""
        if len(kwargs) != 2:
            raise Exception("width and height the only fields")
        for key, value in kwargs.items():
            if type(value) is not int:
                raise TypeError(key + " must be an integer")
            if value < 0:
                raise ValueError(k + " must be >= 0")
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

    s = Square(height=2, width=8)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
