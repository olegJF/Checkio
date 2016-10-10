# -*- coding: utf-8 -*-

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
def isZebra(word):
    zebra = ''
    pair = ''
    for i in word:
        if i in VOWELS:
            zebra +='V'
        elif i in CONSONANTS:
            zebra +='C'
    print(zebra)
    if zebra[0]=='V': pair = 'VC'
    else: pair = 'CV'
    if len(word)%2!=0:
        if zebra[0]!=zebra[-1]:
            return False
        elif zebra[:-1].count(pair)!=len(word)//2:
            return False
        else:
            return True
    else:
        if zebra.count(pair)!=len(word)//2:
            return False
        else:
            return True

            
def checkio(text):
    dot = '.,;:!?'
    count = 0
    text = text.upper()
    for i in dot: text = text.replace(i, ' ')
    array = text.split(' ')
    for word in array:
        if word.isalpha()and len(word)>1:
            
            if isZebra(word):
                print('isZebra word',word)
                count +=1
    return count


print(checkio("Aaaaaaaaaa."))



