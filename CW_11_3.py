# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, len_rec, width = None):
        self.len_rec = len_rec
        if width is None:
            self.width = len_rec
        else: self.width = width
    def perimetr(self):
        return 2 * (self.len_rec + self.width)
    def square(self):
        return self.len_rec * self.width

r = Rectangle(4, 5)
print((r.perimetr()))
print((r.square()))