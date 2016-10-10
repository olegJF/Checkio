# -*- coding: utf-8 -*-

from math import log
def super_root(number):
    x = 1
    while pow(x,x)< number:
        x +=1
    
    if pow(x,x)==number: return x
    
    while abs(x**x - number )>0.0001:
        y = log(number,x)
        x = (x+y)/2
        #res = pow(x,x)
        
        #print('res=',res, ' x=',x)

    return x

print( super_root(2))
