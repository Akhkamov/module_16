class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"Прямоугольник с длиной {self.a} и высотой {self.b}"
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"Квадрат со сторонами {self.a}x{self.a}"
    def get_area(self):
        return self.a**2

class Circle:
    def __init__(self, r):
        self.r = r
    def __str__(self):
        return f"Окружность с радиусом={self.r}"
    def get_area(self):
        return 3.14*self.r**2
