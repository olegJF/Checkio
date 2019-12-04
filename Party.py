'''
вам необходимо создать класс Friend, а каждый друг будет экземпляром
этого класса. Также вам необходимо создать класс Party(place) который будет
отвечать за отправление приглашений.
Периодически круг друзей меняется - иногда появляются новые, иногда исчезают
старые (например, переезжают в другой город). Чтобы наладить взаимодействие
с ними, вам необходимо создать класс Party со следующими методами:

add_friend(Friend(name)) - добавляет друга 'name' в список 'наблюдателей'
    (людей, которые оповещаются каждый раз, когда назначается новая встреча).
del_friend(friend) - удаляет друга friend из списка 'наблюдателей'.
send_invites() - рассылает приглашения всем друзьям из списка 'наблюдателей'.
Класс Friend должен иметь метод show_invite(), который возвращает текст
последнего приглашения, полученного человеком с указанием места, дня и времени.
Место будет указано при создании экземпляра Party. Если человек не получил
приглашения, то этот метод должен вернуть - "No party..."
'''


class Friend:
    def __init__(self, name):
        self._name = name
        self._invite = ''

    def show_invite(self):
        return self._invite if self._invite else "No party..."

    def set_invite(self, invite):
        self._invite = invite


class Party:
    def __init__(self, name):
        self._name = name
        self._friends = []

    def add_friend(self, friend):
        self._friends.append(friend)

    def send_invites(self, date):
        for friend in self._friends:
            friend.set_invite(f'{self._name}: {date}')

    def del_friend(self, friend):
        self._friends.remove(friend)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
