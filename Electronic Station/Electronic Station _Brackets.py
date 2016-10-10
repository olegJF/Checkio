# -*- coding: utf-8 -*-
def checkio(string):
    result = []
    open_brekets = ['(','[','{']
    closed_brekets = [')',']','}']
    for i in string:
        if i in open_brekets:
            result.append(i)
        elif i in closed_brekets:
            y = closed_brekets.index(i)
            if len(result)!=0 and result[-1]== open_brekets[y]:
                result.pop()
            else:
                return False
    if len(result)==0: return True
    
    return False



print(checkio("3+6"))
