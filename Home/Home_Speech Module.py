# -*- coding: utf-8 -*-
data=(32)
a = ['null','one','two','three','four',
         'five','six','seven','eight','nine',
         'ten','eleven','twelve','thirteen',
         'fourteen','fifteen','sixteen',
         'seventeen','eighteen','nineteen','twenty']
b = ['','','twenty','thirty','forty',
         'fifty','sixty','seventy','eighty',
         'ninety','hundred']

def checkio(data):
    if data<21:
        return first_ten(data)
    if data <100:
        return second_ten(data)
    if data<1000:
        hudred = int(str(data)[0:1])
        tens = data-(hudred*100)
        if tens==0:
            return first_ten(hudred)+' hundred'
        elif tens<20:
            return first_ten(hudred)+' hundred '+first_ten(tens)
        return first_ten(hudred)+' hundred '+second_ten(tens)
    
    

def first_ten(number):
    return a[number]

def second_ten(number):
    first = int(number//10)
    second = number-first*10
    if second==0:
        return b[first]
    else:
        return b[first]+' '+a[second]
        
print(checkio(data))


