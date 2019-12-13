class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self._was_hit = 0

    @property
    def is_alive(self):
        return False if self.health <= 0 else True

    def hit(self, power):
        self.health -= power
        self._was_hit = power

    @property
    def was_hit(self):
        return self._was_hit


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.defense = 2

    def hit(self, power):
        if power > self.defense:
            self.health -= (power - self.defense)
            self._was_hit = power - self.defense


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 40
        self.vampirism = 0.5

    def medic(self, power):
        self.health += power * self.vampirism


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6


class Army:

    def __init__(self):
        self.army = []

    def add_units(self, cls_war, how_many):
        self.army += [cls_war() for i in range(how_many)]


class Battle:

    @staticmethod
    def fight(army1, army2):
        unit_1 = army1.army.pop()
        unit_2 = army2.army.pop()
        while any((army1.army, unit_1)) and any((army2.army, unit_2)):
            if not unit_1:
                unit_1 = army1.army.pop()
            if not unit_2:
                unit_2 = army2.army.pop()
            power1 = unit_1.attack
            power2 = unit_2.attack
            r = 1
            while True:
                print(
                    f'round: {r}, Def: {unit_1.health}, Vamp: {unit_2.health}')
                r += 2
                unit_2.hit(power1)
                if isinstance(unit_1, Vampire):
                    power = unit_2.was_hit
                    unit_1.medic(power)
                if isinstance(unit_1, Lancer):
                    next_unit = army2.army[-1] if army2.army else None
                    if next_unit:
                        next_unit.hit(power1 // 2)
                if not unit_2.is_alive:
                    unit_2 = None
                    break
                unit_1.hit(power2)
                if isinstance(unit_2, Vampire):
                    power = unit_1.was_hit
                    unit_2.medic(power)
                if isinstance(unit_2, Lancer):
                    next_unit = army1.army[-1] if army1.army else None
                    if next_unit:
                        next_unit.hit(power2 // 2)
                if not unit_1.is_alive:
                    unit_1 = None
                    break
        if len(army1.army) == 0 and len(army2.army) == 0:
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
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
