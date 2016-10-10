# -*- coding: utf-8 -*-

def checkio(n, m):
    n = bin(n)[2:]
    m = bin(m)[2:]
    """ 
    xor = int(n)^int(m)
    res = 0
    for i in str(xor):
        if i=='1':
            res +=1

    """
    bit = 0
    res = 0
    if len(n)>len(m):
        bit = len(n)-len(m)
        for x in range(bit):
            m = '0'+m
    else:
        bit = len(m)-len(n)
        for x in range(bit):
            n = '0'+n
    for i in range(len(n)):
        if n[i]=='1' and m[i]!='1':
            res +=1
        elif m[i]=='1' and n[i]!='1':
            res +=1
       
    return res



print(checkio(117, 17))
