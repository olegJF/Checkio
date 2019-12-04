"""
    добавить к уже существующим классам и функциям новые:
    Army, который будет обладать методом add_units(),
    позволяющим добавлять выбранное количество воинов в армию,
    а также класс Battle() с функцией fight(), которая будет устраивать
    сражения и определять сильнейшую армию.
    Сражения между армиями происходят по следующему принципу:
    • сперва проводится дуэль между первым воином первой армии и
        первым воином второй
    • как только один из них погибает — в дуэль вступает следующий воин из
        той армии, которая потеряла бойца, а выживший воин со своим
        текущим здоровьем продолжает сражаться
    • так продолжается до тех пор, пока все воины одной из армий не умрут.
        В этом случае функция battle() возвращает True, если первая армия
        выиграла или False, если вторая оказалась сильнее.
    """

# Taken from mission The Warriors

class Warrior():

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return False if self.health <= 0 else True

    def hit(self, power):
        self.health -= power
     

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


class Army():

    def __init__(self):
        self.army = []

    def add_units(self, cls_war, how_many):
        self.army += [cls_war() for i in range(how_many)]


class Battle():

    def fight(self, army1, army2):
        unit_1 = army1.army.pop()
        unit_2 = army2.army.pop()
        while any((army1.army, unit_1)) and any((army2.army, unit_2)):
            if not unit_1:
                unit_1 = army1.army.pop()
            if not unit_2:
                unit_2 = army2.army.pop()
            power1 = unit_1.attack
            power2 = unit_2.attack
            while True:
                unit_2.hit(power1)
                if not unit_2.is_alive:
                    unit_2 = None
                    break
                unit_1.hit(power2)
                if not unit_1.is_alive:
                    unit_1 = None
                    break
        if len(army1.army) == 0  and len(army2.army) == 0:
            return True if unit_1 else False
        return True if army1.army else False

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
    #These "asserts" using only for self-checking and not necessary for auto-testing
   
    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
  
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()
    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

