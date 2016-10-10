# -*- coding: utf-8 -*-
def checkio(text):
    count = 0
    words = text.split(' ')
    for word in words:
        if word.isalpha():
            count +=1
            if count==3: return True
        else: count = 0
    return False

print(checkio("Hello World hello"))
