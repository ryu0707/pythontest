class Apple():

    def __init__(self, color, weight, stem_length, circumference):

        self.color = color

        self.weight = weight

        self.stem_length = stem_length

        self.circumference = circumference

import math

class circle():
    def __init__(self,a):
        self.length = a

    def area(self):
        return self.length * self.length * math.pi

aa = circle(5)
print(aa.area())

class triangle():
    def __init__(self,l,h):
        self.len = l
        self.height = h

    def area(self):
        return self.len * self.height / 2

bb = triangle(10,5)
print(bb.area())


class Hexagon():

    def __init__(self, s1, s2, s3, s4, s5, s6):

        self.s1 = s1

        self.s2 = s2

        self.s3 = s3

        self.s4 = s4

        self.s5 = s5

        self.s6 = s6



    def calculate_perimeter(self):

        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6



a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)

print(a_hexagon.calculate_perimeter())
