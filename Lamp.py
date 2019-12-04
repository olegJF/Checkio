"""
Ваша задача - реализовать класс Lamp() (лампочка) и метод light(),
который будет заставлять лампочку загораться очередным цветом в
последовательности (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’) при каждом включении.
Если в данный момент цвет лампочки - Yellow, то при следующем включении
она загорится зеленым (Green) и так далее.
"""


class Lamp:

    def __init__(self):
        self.cnt = -1
        self.color = ['Green', 'Red', 'Blue', 'Yellow']

    def light(self):
        self.cnt += 1
        index = self.cnt % 4
        return self.color[index]


if __name__ == '__main__':

    lamp_1 = Lamp()
    lamp_2 = Lamp()
    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"

    print("Coding complete? Let's try tests!")

'''
from itertools import cycle


class Lamp:
    def __init__(self):
        self.colour = cycle(("Green", "Red", "Blue", "Yellow"))

    def light(self):
        return next(self.colour)
'''
