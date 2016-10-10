# -*- coding: utf-8 -*-

def checkio(array):
    array = list(array)
    for i in range(len(array)-1):
        for x in range(len(array)-1):
            if abs(array[x])>abs(array[x+1]):
                array[x],array[x+1]=array[x+1],array[x]
    return array
#return sorted(array , key = lambda x: abs(x))    

   
     
    

print(checkio((-1, -2, -3, 0)))
