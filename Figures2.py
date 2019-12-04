from math import pi


class Parameters:

    def __init__(self, param):
        self._param = param
        self._figure = None

    def choose_figure(self, figure):
        self._figure = figure

    def area(self):
        formula = self._figure.formula_area.format(self._param)
        return self.for_print(formula)

    def perimeter(self):
        formula = self._figure.formula_perimeter.format(self._param)
        return self.for_print(formula)

    def volume(self):
        if self._figure.formula_volume:
            formula = self._figure.formula_volume.format(self._param)
            return self.for_print(formula)
        return 0

    @staticmethod
    def for_print(formula):
        value = float(eval(formula))
        if value.is_integer():
            return value
        return round(value, 2)


class Circle:

    def __init__(self):
        self.formula_area = 'pi * {} ** 2'
        self.formula_perimeter = 'pi * {} * 2'
        self.formula_volume = 0


class Triangle:

    def __init__(self):
        self.formula_area = '(3**0.5 * {} ** 2)/4'
        self.formula_perimeter = '3 * {}'
        self.formula_volume = 0


class Square:

    def __init__(self):
        self.formula_area = '{} ** 2'
        self.formula_perimeter = '4 * {}'
        self.formula_volume = 0


class Pentagon:

    def __init__(self):
        self.formula_area = '1.720477401 * {} ** 2'
        self.formula_perimeter = '5 * {}'
        self.formula_volume = 0


class Hexagon:

    def __init__(self):
        self.formula_area = '2.598076211 * {} ** 2'
        self.formula_perimeter = '6 * {}'
        self.formula_volume = 0


class Cube:

    def __init__(self):
        self.formula_area = '6 * {} ** 2'
        self.formula_perimeter = '12 * {}'
        self.formula_volume = '{} ** 3'


if __name__ == '__main__':

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
