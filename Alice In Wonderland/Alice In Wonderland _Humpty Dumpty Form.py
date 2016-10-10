# -*- coding: utf-8 -*-

            
def checkio(a,b):
    from math import pi, sqrt, asin, atanh
    a,b = a/2,b/2
    pair = []
    if a == b:
        volume = round((4*pi*a**3)/3, 2)
        surface = round(4*pi*a**2 , 2)
    elif a > b:
        volume = round((4*pi*b**2*a)/3, 2)
        e = sqrt(1-(b**2/a**2))
        surface = round(2*pi*b**2*(1+((a*asin(e))/(b*e))), 2)
    else:
        volume = round((4*pi*b**2*a)/3, 2)
        e = sqrt(1-(a**2/b**2))
        surface = round(2*pi*b**2*(1+(((1-e**2)*atanh(e))/e)), 2)
        
    pair.append(volume)
    pair.append(surface)
    return pair 



print(checkio(2,4))
