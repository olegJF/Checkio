def checkio(first, second):
    operation = ('&', '|', '^')
    second_len = len(bin(second)[2:])
    first_bin = bin(first)[2:]
    dgts = [int(b*second_len, 2) for b in first_bin]
    return sum(eval(f'{second} {sign} {dgt}'
                   ) for sign in operation for dgt in dgts)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
    print('OK')
