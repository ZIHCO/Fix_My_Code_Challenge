#!/usr/bin/python3
"""This module contains the class, Square"""


class Square():
    """This class create square objects"""

    def __init__(self, width=0, height=0):
        """instantiate an object"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.height = height
        self.width = width

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
    """test code"""

    s = Square()
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
