"""Класс Text должен иметь следующие методы:
write(text) - добавляет указанный текст к текущему.
set_font(font name) - устанавливает шрифт текста. Шрифт распространяется на
весь текст, даже добавленный после установки шрифта и отображается в
квадратных скобках перед началом текста и после конца:
"[Arial]...example...[Arial]".
Шрифт может быть задан сколько угодно раз, но отображается только
последний из них.
show() - отображает текущий текст и шрифт (если задан).
restore(SavedText.get_version(number)) - возвращает текст к указанной версии.

Класс SavedText должен иметь следующие методы:
save_text(Text) - сохраняет текущее состояние текста и текущий шрифт.
Первая сохраненная версия имеет номер 0, вторая - 1 и так далее.
get_version(number) - метод используется вместе с методом restore класса
Text и служит для выбора нужной версии текста.
"""


class Text:
    def __init__(self):
        self._font = ''
        self._text = ''
        self._version = []

    def write(self, text):
        self._text += text
        self._version.append({'text': self._text, 'font': self._font})

    def restore(self, version):
        self._version = self._version[:version + 1]
        self._text = self._version[-1]['text']

    def set_font(self, font):
        for pair in self._version:
            if pair['font'] != '':
                pair['font'] = f'[{font}]'
        self._font = f'[{font}]'

    def show(self):
        data = self._version[-1]
        return f'{data["font"]}{data["text"]}{data["font"]}'



class SavedText:

    def __init__(self):
        self._saved_text = None

    def save_text(self, text):
        self._saved_text = text

    def get_version(self, ver):
        return ver


if __name__ == '__main__':

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "
    text_4 = Text()
    saver_4 = SavedText()
    text_4.write("1. Python ")
    saver_4.save_text(text_4)
    text_4.set_font("Times New Roman")
    text_4.write("2. JavaScript ")
    saver_4.save_text(text_4)
    text_4.write("3. C# ")
    text_4.set_font("Arial")
    saver_4.save_text(text_4)
    text_4.write("4. Java ")
    text_4.write("5. C++ ")
    text_4.restore(saver_4.get_version(2))
    print(text_4.show())
    assert text_4.show() == '[Arial]1. Python 2. JavaScript 3. C# [Arial]'

    text_5 = Text()
    saver_5 = SavedText()
    text_5.write("first part ")
    saver_5.save_text(text_5)
    text_5.write("second part ")
    saver_5.save_text(text_5)
    text_5.write("third part ")
    saver_5.save_text(text_5)
    text_5.write("fourth part ")
    text_5.write("fifth part ")
    text_5.restore(saver_5.get_version(0))
    text_5.write("is empty")
    assert text_5.show() == 'first part is empty'
    print("Coding complete? Let's try tests!")
