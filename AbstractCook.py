"""
    работают 3 повара: JapaneseCook, RussianCook и ItalianCook.
    Каждый из них умеет готовить блюдо и напиток национальной кухни:
    - JapaneseCook: Sushi и Tea
    - RussianCook: Dumplings и Compote
    - ItalianCook: Pizza и Juice
    Ваша задача - реализовать 3 класса (каждый повар - отдельный класс), которые будут
    наследниками AbstractCook с соответствующими методами:
    - add_food(food_amount, food_price), который добавляет в заказ клиента
        указанное количество еды по указанной цене
    - add_drink(drink_amount, drink_price), который добавляет в заказ клиента
        указанное количество напитков по указанной цене
    - total(), который возвращает строку вида: 'Food: 150, Drinks: 50, Total: 200',
        причем для каждого повара на месте Food и Drinks будут указаны именно те
        блюда и напитки, которые он готовит.
    Обратите внимание, что каждый клиент может обращаться только к одному повару.
"""
class AbstractCook:

    def __init__(self):
        self._food = 0
        self._drink = 0
        self._total = 0

    def add_food(self, qty, price):
        self._food += qty * price

    def add_drink(self, qty, price):
        self._drink += qty * price

    def _total_string(self, food_name, drink_name):
        self._total += self._drink
        self._total += self._food
        return f"{food_name}: {self._food}, {drink_name}: {self._drink}, Total: {self._total}"


class JapaneseCook(AbstractCook):

    def total(self):
        return self._total_string('Sushi', 'Tea')


class RussianCook(AbstractCook):

    def total(self):
        return self._total_string('Dumplings', 'Compote')


class ItalianCook(AbstractCook):

    def total(self):
        return self._total_string('Pizza', 'Juice')

#
# def class_factory(food_name, drink_name):
#     class T:
#
#         def __init__(self):
#             self.food = self.drink = 0
#
#         def add_food(self, food_amount, food_price):
#             self.food += food_amount * food_price
#
#         def add_drink(self, drink_amount, drink_price):
#             self.drink += drink_amount * drink_price
#
#         def total(self):
#             return f'{food_name}: {self.food}, {drink_name}: {self.drink}, Total: {self.food + self.drink}'
#
#     return T
#
#
# JapaneseCook = class_factory('Sushi', 'Tea')
#
# RussianCook = class_factory('Dumplings', 'Compote')
#
# ItalianCook = class_factory('Pizza', 'Juice')


if __name__ == '__main__':
    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    print(client_1.total() == "Sushi: 105, Tea: 20, Total: 125")
    print("Coding complete? Let's try tests!")

