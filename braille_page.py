import string


def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)


def adder(_res, _char):
    if not _res[0]:
        for y, _lst in enumerate(_res):
            _lst.extend(_char[y])
    else:
        for y, _lst in enumerate(_res):
            _lst.extend([0])
            if _char:
                _lst.extend(_char[y])
    return _res


def braille_page(text: str):
    alphabet = string.ascii_lowercase
    max_len = 29
    separator = [0 for i in range(max_len)]
    is_full_line = False
    rows = []
    tmp = [[], [], []]
    res = []
    for i, char in enumerate(text):
        chars = []
        if len(tmp[0]) == max_len:
            rows.append(tmp)
            tmp = [[], [], []]
            is_full_line = True
            if i != len(text) - 1:
                rows.append([separator])
        if char.isdigit():
            dgt = int(char)
            indx = dgt - 1 if dgt != 0 else 9
            chars.extend([NUMBER_FORMAT, LETTERS_NUMBERS[indx]])
        elif char.isalpha():
            if char.istitle():
                chars.extend([CAPITAL_FORMAT])
            chars.extend([LETTERS_NUMBERS[alphabet.index(char.lower())]])
        elif char.isspace():
            chars.extend([WHITESPACE])
        else:
            chars.extend([PUNCTUATION[char]])
        for ch in chars:
            tmp = adder(tmp, ch)
            if len(tmp[0]) == max_len:
                is_full_line = True
                rows.append(tmp)
                tmp = [[], [], []]
                if i != len(text) - 1:
                    rows.append([separator])
    if tmp[0]:
        rows.append(tmp)
    size = len(rows[-1][0])
    if size != max_len and is_full_line:
        for i in range(max_len-size):
            rows[-1] = adder(rows[-1], [])
    for row in rows:
        res.extend(row)
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, text, answer):
        result = func(text)
        _res = tuple(tuple(row) for row in result)
        return answer == tuple(tuple(row) for row in result)

    # assert checker(braille_page, "hello 1st World!", (
    #     (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
    #     (1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
    #     (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
    # ), "Example"
    # assert checker(braille_page, "42", (
    #     (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
    #     (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0),
    #     (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))), "42"
    # assert checker(braille_page, "CODE", (
    #     (0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
    #     (0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0))
    # ), "CODE"
    assert checker(braille_page, "0123456789",(
        (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1),
        (0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
        (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))
                   )
    print('OK')
