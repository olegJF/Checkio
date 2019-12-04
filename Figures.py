from math import pi


class Parameters:

    def __init__(self, param):
        self._param = param
        self._figure = None

    def choose_figure(self, figure):
        self._figure = figure

    def area(self):
        return self._figure.area(self._param)

    def perimeter(self):
        return self._figure.perimeter(self._param)

    def volume(self):
        return self._figure.volume(self._param)


class Figure:

    def for_print(self, value):
        if value.is_integer():
            return value
        return round(value, 2)


class Circle(Figure):

    def area(self, param):
        return self.for_print(float(pi * param ** 2))

    def perimeter(self, param):
        return self.for_print(float(pi * param * 2))

    def volume(self, param):
        return 0


class Triangle(Figure):

    def area(self, param):
        return self.for_print(float((3**0.5 * param ** 2)/4))

    def perimeter(self, param):
        return self.for_print(float(3 * param))

    def volume(self, param):
        return 0


class Square(Figure):

    def area(self, param):
        return self.for_print(float(param ** 2))

    def perimeter(self, param):
        return self.for_print(float(4 * param))

    def volume(self, param):
        return 0


class Pentagon(Figure):

    def area(self, param):
        return self.for_print(float(1.720477401 * param ** 2))

    def perimeter(self, param):
        return self.for_print(float(5 * param))

    def volume(self, param):
        return 0


class Hexagon(Figure):

    def area(self, param):
        return self.for_print(float(2.598076211 * param ** 2))

    def perimeter(self, param):
        return self.for_print(float(6 * param))

    def volume(self, param):
        return 0


class Cube(Figure):

    def area(self, param):
        return self.for_print(float(6 * param ** 2))

    def perimeter(self, param):
        return self.for_print(float(12 * param))

    def volume(self, param):
        return self.for_print(float(param ** 3))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
