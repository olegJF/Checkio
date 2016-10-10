# -*- coding: utf-8 -*-
            
def checkio(num):
    fibo = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    transperent = 10000
    age = 0
    while transperent!=num:
        age += 1
        #print('trans=', transperent)
        if age in fibo:
            transperent -= age
            #print('age=', age)
        else:
            transperent +=1
            #print('else  age=', age)
        
    return age


print(checkio(9990))



