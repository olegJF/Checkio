# -*- coding: utf-8 -*-
def checkio(*args):
    args = list(args)
    if len(args)==0: return 0
    return max(args)-min(args)
    

print(checkio(10.2, -2.2, 0, 1.1, 0.5))
