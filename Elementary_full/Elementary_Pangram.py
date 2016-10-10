# -*- coding: utf-8 -*-

def checkio(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    if len(text)<26:
        return False
    for letter in alphabet:
        if text.count(letter)==0:
            return False
    return True
    #return len([x for x in string.ascii_lowercase if x not in text.lower()]) == 0
    #return set(string.ascii_lowercase) <= set(text.lower())
        



    
     
    

print(checkio('The! quick. brown ,fox jumps? over# the lazdog'))
