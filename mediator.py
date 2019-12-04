VOWELS = 'aeiou'


class Member:

    def __init__(self, name) -> None:
        self.name = name
        self._chat = None

    @staticmethod
    def converter(message):
        return ''.join('0' if c in VOWELS else '1' for c in message.lower())

    def send(self, message):
        self._chat.send(f"{self.name} said: {message}")
        self._chat.send_to_robot_dialogue(
            f"{self.name} said: {self.converter(message)}")

    def connect_to_chat(self, chat):
        self._chat = chat


class Human(Member):
    pass


class Robot(Member):
    pass


class Chat:

    def __init__(self) -> None:
        self._human = None
        self._robot = None
        self._dialog = []
        self._robot_dialogue = []

    def connect_human(self, human: Human) -> None:
        """
        Привязывает к каналу человека
        """
        self._human = human
        self._human.connect_to_chat(self)

    def connect_robot(self, robot: Robot) -> None:
        """
        Привязывает к каналу робота
        """
        self._robot = robot
        self._robot.connect_to_chat(self)

    def send(self, message):
        self._dialog.append(message)

    def send_to_robot_dialogue(self, message):
        self._robot_dialogue.append(message)

    def show_human_dialogue(self):
        return '\n'.join(self._dialog)

    def show_robot_dialogue(self):
        return '\n'.join(self._robot_dialogue)


if __name__ == "__main__":
    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_human_dialogue())
    print(chat.show_robot_dialogue())
