class Shape:
    def init(self, a):
        self.a = a

    def show_data(self):
        pass

    def perimetr(self):
        pass

class Circle(Shape):
    def init(self, a):
        super().init(a)

    def perimetr(self):
        return f'{(self.a*3.14)*2} cm'
    def show_data(self):
        return f'узундугу {self.a} см'

class Rectangle(Circle):
    def init(self, a, b):
        super().init(a)
        self.b = b

    def perimetr(self):
        return f'{(self.a + self.b ) * 2} cm'
    def show_data(self):
        return f'узуну {self.a}, туурасы {self.b}'

class Triangle(Rectangle):
    def init(self, a, b, c):
        super().init(a, b)
        self.c = c

    def perimetr(self):
        return f'{self.a*self.b*self.c} см '
    def show_data(self):
        return f'a = {self.a}, b = {self.b}, c = {self.c}'

circle1 = Circle(5)
print(circle1.show_data())
print(circle1.perimetr())