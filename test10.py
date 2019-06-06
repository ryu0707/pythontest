class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)
        
    def calculate_perimeter(self):
        return self.s1 * 4
    
    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1)

a_square = Square(29)
print(a_square)


def compare(a1,a2):
    return a1 is a2

print(compare(1,1))
