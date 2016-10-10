# -*- coding: utf-8 -*-

def checkio(a,b):
    
    import math
    try:
        return int(math.pow(a[b],b))
    except:
        return -1
    
        
    
    

print(checkio([1, 2], 3))
