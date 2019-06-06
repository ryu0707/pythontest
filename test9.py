class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2

    def calculate_perimeter(self):
        return (self.s1 * 2) + (self.s2 * 2)

class Square(Shape):
    def __init__(self,s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 -= new_size

a_rectangle = Rectangle(5,10)
a_square = Square(20)
print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

a_square.change_size(5)
print(a_square.calculate_perimeter())

a_rectangle.what_am_i()
a_square.what_am_i()


class Horse:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self,name):
        self.name = name

a_rider = Rider("Ryota")
a_horse = Horse("Teio","aaa",a_rider)
print(a_horse.owner.name)
