# -*- coding: utf-8 -*-
def checkio(text):
    message = ''
    for i in text:
        if i.isupper(): message +=i
    
    return message

print(checkio("How are you? Eh, ok. Low or Lower? Ohhh."))
