"""
 вам необходимо будет создать класс Warrior, у экземпляров которого будет
 2 параметра — здоровье (равное 50) и атака (равная 5), а также свойство
 is_alive, которое может быть True (если здоровье воина > 0) или False
 (в ином случае). Кроме этого вам необходимо создать класс для второго типа
 солдат — Knight, который будет наследником Warrior, но
 с увеличенной атакой — 7. Также вам необходимо будет создать функцию fight(),
 которая будет проводить дуэли между 2 воинами и определять сильнейшего из них.
 Бои происходят по следующему принципу:
• каждый ход первый воин наносит второму урон в размере своей атаки,
    в следствие чего здоровье второго воина уменьшается
• аналогично поступает и второй воин по отношению к первому.
Если в конце очередного хода у первого воина здоровье > 0, а у другого — нет,
выживший объявляется победителем и функция возвращает True, или
False в ином случае
"""


class Warrior():
    def __init__(self):

        self.health = 50

        self.attack = 5

        self.is_alive = True


    def hit(self, power):

        self.health -= power

        if self.health < 0:

            self.is_alive = False


class Knight(Warrior):

    def __init__(self):

        Warrior.__init__(self)

        self.attack = 7




def fight(unit_1, unit_2):

    power1 = unit_1.attack

    power2 = unit_2.attack

    while True:

        unit_2.hit(power1)

        if not unit_2.is_alive:

            return True

        unit_1.hit(power2)

        if not unit_1.is_alive:

            return False


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing


    chuck = Warrior()

    bruce = Warrior()

    carl = Knight()

    dave = Warrior()

    mark = Warrior()


    assert fight(chuck, bruce) == True

    assert fight(dave, carl) == False

    assert chuck.is_alive == True

    assert bruce.is_alive == False

    assert carl.is_alive == True

    assert dave.is_alive == False

    assert fight(carl, mark) == False

    assert carl.is_alive == False


    print("Coding complete? Let's try tests!")

