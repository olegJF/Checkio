# -*- coding: utf-8 -*-

def left_join(phrases):
    text = ''
    for word in phrases: text +=word+','
    text = text[:-1]
    text = text.replace('right','left')

    return text
     
    

print(left_join(("enough", "jokes")))
