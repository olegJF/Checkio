def middle(text):
    size = len(text)
    if size == 1:
        return text
    return text[size // 2] if size % 2 else text[size // 2-1: size // 2+1]

if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")
