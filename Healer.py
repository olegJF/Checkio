'''
Healer не будет сражаться лично (его атака равна 0 и он не сможет
нанести урон), но его задача не менее полезна - каждый раз,
когда союзный солдат бьет врага, Healer, стоящий позади союзника лечит его
на +2 единицы здоровья с помощью метода heal(). При этом исцеление не может
поднять здоровье выше максимального уровня. То есть, если Healer лечит Warrior,
у которого 49 единиц здоровья, то после лечения Warrior будет иметь 50 единиц
здоровья, так как это - его максимальный уровень.
Базовые параметры класса Healer:
health = 60
attack = 0
'''


class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self._was_hit = 0
        self.max_health = self.health

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
        self.max_health = self.health

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
        self.max_health = self.health

    def medic(self, power):
        self.health += power * self.vampirism


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0
        self._heal = 2
        self.max_health = self.health

    def heal(self, patient):
        _health = patient.health + self._heal
        patient.health = _health if _health <= patient.max_health \
            else patient.max_health



class Army:

    def __init__(self):
        self.army = []

    def add_units(self, cls_war, how_many):
        self.army += [cls_war() for i in range(how_many)]


class Battle:

    @staticmethod
    def fight(army1, army2):
        army1 = list(reversed(army1.army))
        army2 = list(reversed(army2.army))
        unit_1 = army1.pop()
        unit_2 = army2.pop()
        round = 2
        while any((army1, unit_1)) and any((army2, unit_2)):
            if not unit_1:
                unit_1 = army1.pop()
            if not unit_2:
                unit_2 = army2.pop()
            power1 = unit_1.attack
            power2 = unit_2.attack
            while True:
                next_unit_1 = army1[-1] if army1 else None
                next_unit_2 = army2[-1] if army2 else None

                unit_2.hit(power1)
                if isinstance(unit_1, Vampire):
                    power = unit_2.was_hit
                    unit_1.medic(power)
                if isinstance(unit_1, Lancer) and next_unit_2:
                    next_unit_2.hit(power1 // 2)
                if isinstance(next_unit_1, Healer):
                    next_unit_1.heal(unit_1)
                # print(f'Round: {round}, L:{unit_1.health}, W:{unit_2.health}, H: {next_unit_2.health}')
                round += 1
                if not unit_2.is_alive:
                    unit_2 = None
                    break

                unit_1.hit(power2)
                if isinstance(unit_2, Vampire):
                    power = unit_1.was_hit
                    unit_2.medic(power)
                if isinstance(unit_2, Lancer) and next_unit_1:
                    next_unit_1.hit(power2 // 2)
                if isinstance(next_unit_2, Healer):
                    next_unit_2.heal(unit_2)
                # print(f'Round: {round}, L:{unit_1.health}, W:{unit_2.health}, H: {next_unit_2.health}')
                round += 1
                if not unit_1.is_alive:
                    unit_1 = None
                    break
        if len(army1) == 0 and len(army2) == 0:
            return True if unit_1 else False
        return True if army1 else False


def fight(unit_1, unit_2):
    power1 = unit_1.attack
    power2 = unit_2.attack
    while True:
        unit_2.hit(power1)
        if isinstance(unit_1, Vampire):
            power = unit_2.was_hit
            unit_1.medic(power)
        if not unit_2.is_alive:
            return True
        unit_1.hit(power2)
        if isinstance(unit_2, Vampire):
            power = unit_1.was_hit
            unit_2.medic(power)
        if not unit_1.is_alive:
            return False


if __name__ == '__main__':
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
    priest = Healer()

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
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    army_5 = Army()
    army_5.add_units(Lancer, 1)

    army_6 = Army()
    army_6.add_units(Warrior, 1)
    army_6.add_units(Healer, 1)


    battle = Battle()
    # battle.fight(army_5, army_6)
    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
