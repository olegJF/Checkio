# -*- coding: utf-8 -*-

def checkio(number):
    tmp = '00123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_k = max(set(number))
    begin = tmp.find(max_k)
    for i in range(begin, 37):
        try:
            n = int(number,i)
            if n%(i-1) == 0:
                return i
        except: pass
    return 0

print(checkio("IDDQD"))

