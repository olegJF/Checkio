# -*- coding: utf-8 -*-

def chase(a1, t2, time):
    x = (t2*time)/(a1-t2)
    if (t2*time)%(a1-t2): return round(x, 8)+time
    return int(x)+time
    

print(chase(6, 3, 2))
    
