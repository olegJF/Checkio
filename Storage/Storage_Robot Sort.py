# -*- coding: utf-8 -*-

def swapsort(array):
    array = list(array)
    tmp = array[:]
    if tmp == sorted(array): return ''
    res = []
    size = len(tmp)-1
    while tmp != sorted(array):
        for i in range(size):
            if tmp[i]>tmp[i+1]:
                tmp[i],tmp[i+1] = tmp[i+1],tmp[i]
                res.append(str(i)+str(i+1))
                break
    return ','.join(res)
                           
print(swapsort((1, 2, 3, 4, 5)))

