import string
def to_decrypt(cryptotext, delta):
    etalon = string.ascii_lowercase
    res = ''
    for s in cryptotext:
        if s == ' ':
            res += s
        else:
            if s.isalpha():
                index = (etalon.find(s) + delta) % len(etalon)
                res += etalon[index]
    return res

if __name__ == '__main__':
    print("Example:")
    print(to_decrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")
