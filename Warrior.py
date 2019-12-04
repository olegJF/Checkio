
class Warrior():

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return False if self.health < 0 else True


    def hit(self, power):
        self.health -= power
        

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
    #These "asserts" using only for self-checking and not necessary for auto-testing
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

