# -*- coding: utf-8 -*-
def checkio(text, words):
    text = text.lower()
    count = 0
    for word in words:
        if text.find(word)!=-1: count +=1
    return count

print(checkio("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}))
