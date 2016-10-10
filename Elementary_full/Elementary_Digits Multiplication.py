# -*- coding: utf-8 -*-

def checkio(number):
    summ =1
    for i in str(number):
        if i !='0': summ *= int(i)
    return summ
     
    

print(checkio(1111111))
