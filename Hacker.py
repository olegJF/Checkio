'''Вы с друзьями решили почувствовать себя настоящими хакерами и для этого
необходимо было выбрать специальный язык для общения в сети, понятный только
вам. После долгих размышлений, вы решили что в оригинале сообщения будут
на английском языке с возможностью написания времени в формате "hh:mm" и
даты в формате "dd.mm.yyyy". Также (помимо "." и ":") могут использоваться
символы "!", "?", "$", "%", "@".
После того, как сообщение написано и готово к отправке - его необходимо
зашифровать по следующему принципу:
- все буквы и пробелы сперва преобразовываются в соответствующие ASCII коды,
    а затем каждое полученное таким образом число преобразовывается в двоичное
    число, за исключением пробела - пробел должен быть отображен как "1000000",
    а не "100000".
- числа, даты, время и специальные символы, описанные выше, не изменяются.
    После этого сообщение будет готово к отправке.

Для реализации этой системы вам необходимо создать класс HackerLanguage
с соответствующие методами для работы с текстом. Команды, которые будут
использоваться:

write(text) - дописывает к текущему тексту сообщения новый текст (text).
delete(N) - удаляет из текущего сообщения последние N символов.
send() - возвращает зашифрованное сообщение, которое будет отправлено.
read(text) - в качестве аргумента получает зашифрованное сообщение и
возвращает его как обычный английский текст.
'''


class TranslatorMixin:
    def send(self):
        res = ''
        for l in self._text:
            if l.isalpha():
                res += bin(ord(l))[2:]
            elif l == ' ':
                res += '1000000'
            else:
                res += l
        return res

    @staticmethod
    def read(code):

        def from_bin_to_chars(some_code):
            _tmp = ''
            for i in range(0, len(some_code), 7):
                _tmp += (chr(int(some_code[i:i + 7], 2)))
            return _tmp

        words = code.split('1000000')
        res = []
        for word in words:
            tmp = ''
            if len(set(word)) == 2:
                tmp = from_bin_to_chars(word)
            elif word[-1] == ':':
                tmp = from_bin_to_chars(word[-1])
                tmp += ":"
            elif ':' in word:
                index = word.find(':')
                clock = word[:index+3]
                am_pm = from_bin_to_chars(word[index+3:])
                tmp = clock + am_pm
            else:
                while word:
                    c = word[0]
                    word = word[1:] if len(word) >= 2 else ''
                    if c != '1' and c != '0':
                        tmp += c
                    else:
                        if word:
                            if word[0] != '1' and word[0] != '0':
                                tmp += c
                            else:
                                s_code = c + word[:6]
                                tmp += from_bin_to_chars(s_code)
                                word = word[6:]
                        else:
                            tmp += c
            res.append(tmp)
        return ' '.join(res)


class HackerLanguage(TranslatorMixin):
    def __init__(self):
        self._text = ''

    def write(self, text):
        self._text += text

    def delete(self, number):
        self._text = self._text[:-number]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()
    assert message_1.send() == "111001111001011100011111001011001011110100"

    assert message_2.read("11001011101101110000111010011101100") == "email"

    message_1 = HackerLanguage()
    message_1.write('Remember: 21.07.2018 at 11:11AM')
    message_1.delete(2)
    message_1.write('PM')
    assert message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'
    message_2 = HackerLanguage()
    assert message_2.read(
        '10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') == 'My email is mr.robot@gmail.com'

    print('OK')
