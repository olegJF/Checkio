"""
 Вам необходимо создать класс Person, а также несколько методов для работы с
 его экземплярами. Описание класса смотрите далее.

class Person(first_name, last_name, birth_date, job, working_years, salary,
                    country, city, gender='unknown')

Возвращает новый экземпляр класса Person c именем и фамилией
[first_name, last_name], датой рождения - birth_date (в формате 'dd.mm.yyyy'),
текущим местом работы - job, количеством проработанных лет - working_years,
средней зарплатой за весь период работы - salary (сумма в месяц),
страной и городом проживания - [country, city] и полом - gender.
Параметр gender может принимать значения 'male' или 'female'.
Если этот параметр не задан, то значение по умолчанию - 'unknown'.
Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’) ==
Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’)


Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’) ==
Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’, ‘unknown’)


name() Возвращает полное имя (имя и фамилию, разделенные пробелом).
Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600,
‘Canada’, ‘Vancouver’, ‘male’).name() == ‘John Smith’



age() Возвращает возраст человека - количество полных прожитых лет.
(Считайте текущим днем 01.01.2018)
Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’,
‘Vancouver’, ‘male’).age() == 38

work() Возвращает род занятий человека в предложении вида:
‘He is a ...’ (если male) ‘She is a ...’ (female) ‘Is a ...’ (unknown)
В зависимости того, какой пол человека задан (м/ж) или, если пол
неопределен - возвращает без указания пола.
Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150,
 ‘Austria’, ‘Vienna’).work() == ‘Is a designer’

money() Возвращает количество денег, заработанное за весь период работы. Сумму
следует выводить в формате xx xxx … - разбивая каждых 3 разряда пробелами.
Например: ‘10 568’ ‘1 051 422’
Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600,
‘Canada’, ‘Vancouver’, ‘male’).money() == ‘648 000’

home() Возвращает страну и город проживания в формате: ‘Lives in city, country’
Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’,
‘Vienna’).home() == ‘Lives in Vienna, Austria’

"""
import datetime


class Person:
    def __init__(self, first_name, last_name, birth_date, job,
                 working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y')
        self.end_date = datetime.datetime(2018, 1, 1)
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender
        self.sex = {'male': 'He is', 'female': 'She is', 'unknown': 'Is'}

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        delta = self.end_date - self.birth_date
        return delta.days // 365.2425

    def work(self):
        return f'{self.sex[self.gender]} a {self.job}'

    def money(self):
        _money = str(self.salary * 12 * self.working_years)
        _dgts = []
        for e in range(len(_money), -1, -3):
            b = e - 3 if e > 3 else 0
            _dgts.append(_money[b: e])
        _dgts = [r for r in reversed(_dgts) if r]
        return ' '.join(_dgts)

    def home(self):
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
