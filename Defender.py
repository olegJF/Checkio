

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


class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 3
        self.health = 60
        self.defense = 2

    def hit(self, power):
        if power > self.defense:
            self.health -= (power - self.defense)


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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
