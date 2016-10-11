# -*- coding: utf-8 -*-
VOWELS = "aeiouy"

def translate(phrase):
    bird_words = phrase.split(' ')
    words = []
    for bird_word in bird_words:
        word = ''
        i = 0
        while i <len(bird_word):
            
            if bird_word[i] in VOWELS:
                word +=bird_word[i]
                i +=3
            else:
                word +=bird_word[i]
                i +=2
        
        words.append(word)    
            
    return ' '.join(words)

print(translate("hoooowe yyyooouuu duoooiiine"))
