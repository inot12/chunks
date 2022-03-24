'''
Created on Mar 19, 2019

@author: toni
'''
import math


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%.d, %.d' % (self.x, self.y)

    def __add__(self, other):
        '''The __add__ method defines the addition of two Point objects.
        It enables the use of the + operator. p1+p2'''
        if isinstance(other, Point):
            return (self.x + other.x, self.y + other.y)
        if isinstance(other, tuple):
            return (self.x + other[0], self.y + other[1])
        raise ValueError('Not supported type. Has to be either object '
                         'Point or a tuple.')

    def __radd__(self, other):
        '''This method enables commutative behavior of operands.
        If not specified, reversing the type of operands would result in an
        TypeError. Because in the elif statement we defined Point+tuple so
        tuple+Point would raise the TypeError.'''
        return self.__add__(other)


class Rectangle:
    """
    Represents the anchor values for a rectangle.

    Attributes: height, width, corner(corner.x, corner.y)
    """

    def __init__(self, height, width, corner, color):
        self.heigth = height
        self.width = width
        self.corner = corner
        self.corner.x = corner.x
        self.corner.y = corner.y
        self.color = color


class Circle:
    '''Circles for World.'''

    def __init__(self, p, r, color):
        self.p = p
        self.p.x = p.x
        self.p.y = p.y
        self.r = r
        self.color = color


def distance_between_points(a, b):
    '''Calculates the distance between two points.'''
    d = math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
    return d


def main():
    t1, t2 = Point(-150, -100), Point(3, 4)
    print(distance_between_points(t1, t2))

    p = Point(2, 5)
    print(p)
    p1 = Point(1, 6)
    print(p + p1)


if __name__ == "__main__":
    main()
