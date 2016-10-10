# -*- coding: utf-8 -*-

def checkio(first, second):
    first = set(first.split(','))
    second = set(second.split(','))
    a = sorted(list(first.intersection(second))) 
    return ','.join(a)

#checkio = lambda f, s: ','.join(sorted(x for x in f.split(',') if x in s.split(',')))


        



    
     
    

print(checkio("one,two,three", "four,five,six"))
