'''
3 микроволновых печи (Мicrowave1, Мicrowave2, Мicrowave3), которые являются
субклассами класса MicrowaveBase. Каждая печь может принимать команды от пульта
дистанционного управления - RemoteControl. Используемые команды:

set_time("xx:xx"), где "xx:xx" - время в минутах и секундах, которое показывает,
    сколько будет разогреваться еда. Например: set_time("05:30")
add_time("Ns"), add_time("Nm"), где N - количество секунд или минут, которое
    нужно добавить к текущему времени.
del_time("Ns"), del_time("Nm"), где N - количество секунд или минут, которое
    нужно отнять от текущего времени.
show_time(), показывает текущее время выставленное на определенной печи.

Время по умолчанию равно 00:00. Обратите внимание, что время не может быть
меньше 00:00 и больше 90:00, даже если add_time или del_time приводят к
подобной ситуации.

Ваша задача - создать все необходимые классы (родительский класс MicrowaveBase,
3 класса для печей и RemoteControl) и реализовать управление каждой
микроволновкой с помощью общего пульта RemoteControl(microwave),
где microwave - одна из 3 микроволновых печей, которой должен управлять пульт
(например, microwave = Microwave1())
Также обратите внимание, что только одна печь нормально отображает
время - Microwave3. Две остальные печи имеют поврежденные дисплеи и на
месте определенного символа отображают лишь "_". Для первой печи такой
символ - первый, для второй - последний.

microwave_1 = Microwave1()
microwave_2 = Microwave2()
microwave_3 = Microwave3()

RemoteControl(microwave_1).show_time() == "_0:00"
RemoteControl(microwave_2).show_time() == "00:0_"
RemoteControl(microwave_3).show_time() == "00:00"
 '''


class MicrowaveBase:

    def __init__(self):
        self._time = '00:00'
        self._mask = '00:00'
        self._max_time = 90 * 60

    def get_dgt(self):
        tmp_time = self._time.split(':')
        tmp_time = int(tmp_time[0]) * 60 + int(tmp_time[1])
        return tmp_time

    @staticmethod
    def time_to_str(seconds):
        _min = seconds // 60
        _min = _min if _min >= 10 else f'0{_min}'
        _sec = seconds % 60
        _sec = _sec if _sec >= 10 else f'0{_sec}'
        return f'{_min}:{_sec}'

    def set_time(self, time):
        self._time = time

    def show_time(self):
        tmp = ''
        for i, sign in enumerate(self._mask):
            if sign != '_':
                tmp += self._time[i]
            else:
                tmp += '_'
        return tmp

    def add_time(self, time):
        tmp_time = self.get_dgt()
        if time[-1] == 's':
            tmp_time += int(time[:-1])
        else:
            tmp_time += int(time[:-1]) * 60
        if tmp_time > self._max_time:
            self._time = '90:00'
        else:
            self._time = self.time_to_str(tmp_time)
        return self._time

    def del_time(self, time):
        tmp_time = self.get_dgt()
        if time[-1] == 's':
            tmp_time -= int(time[:-1])
        else:
            tmp_time -= int(time[:-1]) * 60
        if tmp_time < 0:
            self._time = '00:00'
        else:
            self._time = self.time_to_str(tmp_time)
        return self._time


class Microwave1(MicrowaveBase):

    def __init__(self):
        MicrowaveBase.__init__(self)
        self._mask = '_0:00'


class Microwave2(MicrowaveBase):

    def __init__(self):
        MicrowaveBase.__init__(self)
        self._mask = '00:0_'


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:

    def __init__(self, microwave):
        self._microwave = microwave

    def set_time(self, time):
        self._microwave.set_time(time)

    def show_time(self):
        return self._microwave.show_time()

    def add_time(self, time):
        return self._microwave.add_time(time)

    def del_time(self, time):
        return self._microwave.del_time(time)


if __name__ == '__main__':
    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    print(RemoteControl(microwave_1).show_time() == "_0:00")
    print(RemoteControl(microwave_2).show_time() == "00:0_")
    print(RemoteControl(microwave_3).show_time() == "00:00")

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")
    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")
    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    print(remote_control_1.show_time() == "_1:00")
    print(remote_control_2.show_time())
    print(remote_control_2.show_time() == "01:3_")
    print(remote_control_3.show_time())
    print(remote_control_3.show_time() == "01:40")

