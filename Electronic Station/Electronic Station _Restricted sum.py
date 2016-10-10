# -*- coding: utf-8 -*-
def rekurs(array):
    if array: return array.pop() + rekurs(array)
    else: return 0
        
def checkio(array):
    
    return rekurs(array)
    
    



print(checkio([2,3,4,1]))
