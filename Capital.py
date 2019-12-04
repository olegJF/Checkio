"""Вы - активный путешественник, который побывал уже не в одном десятке
стран мира. Ваш богатый опыт натолкнул вас на мысль, что самые интересные
и передовые вещи в стране проще всего найти в ее столице.
Ваша задача - реализовать класс Capital(), для которого можно было бы создать
только один объект с глобальным доступом к нему, а все последующие
создаваемые экземпляры этого класса не перезаписывали бы первый
(и единственный) экземпляр. Также вам необходимо реализовать метод name()
который возвращает название столицы.
В этой миссии вам может помочь такой шаблон проектирования, как Singleton.
"""
class Capital:
    __instance = None
    def __new__(cls, name):
        if Capital.__instance is None:
            Capital.__instance = object.__new__(cls)
            Capital.__instance._name = name
        return Capital.__instance

    def name(self):
        return self._name


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
