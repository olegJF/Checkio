# -*- coding: utf-8 -*-

def NOD (*args):
    b,a = sorted(args)
    while b!=0:
        a=a%b
        a,b = b,a
        #print (a,b)
    return a

def greatest_common_divisor(*args):
    array = list(args)
    for i in range(len(array)-1):
        array[i+1] = NOD(array[i],array[i+1])
        #array[i+1] = D
        #print(D)
    return array[-1]
    

print(greatest_common_divisor(3, 9))
