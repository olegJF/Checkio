# -*- coding: utf-8 -*-
def getUniq(string):
    key = [i for i in string]
    size = len(key)
    for i in range(1, size):
        if key[:size-i] == key[i:]:
            size = i
            break
    return ''.join(key[:size])
from decimal import *
def convert(num, denom):
    
    getcontext().prec = 101
    if num%denom == 0: return str(num/denom)[:-1]
    else:
        res = str(Decimal(num)/Decimal(denom)).split('.')
        #print(res)
        tmp = ''
        if len(res[1])>10: tmp = res[1][:-1]
        else: tmp =res[1]
        uniq = set(tmp)
        if tmp.count(tmp[0])== len(tmp) and len(tmp)>1:
            return res[0]+'.'+'('+tmp[0]+')'
        elif len(uniq)==len(tmp): return res[0]+'.'+tmp
        else:
            res_str = ''
            for i in range(len(tmp)):
                if  tmp == getUniq(tmp):
                    res_str +=tmp[0]
                    tmp = tmp[1:]
                else:
                    tmp = getUniq(tmp)
                    break
            if tmp and res_str:
                return res[0]+'.'+res_str+'('+tmp+')'
            elif tmp and tmp !=res[1]:
                return res[0]+'.'+'('+tmp+')'
            else:
                return res[0]+'.'+ res_str
                
            

print( convert(1,776))
#58, 23
#1,776
#113,927
def Uniq(string):
    key = [i for i in string]
    size = len(key)
    for i in range(1, size):
        if key[:size-i] == key[i:]:
            size = i
            break
    return ''.join(key[:size])
                   
#a='121898597626752966558791801510248112189859762675296655879180151024811218985976267529665587918015102481'
#print(Uniq(a))
"""
key,lastind, i =[],1, 0
    for letter in string:
        key.append(letter)
        if letter!=key[i%lastind]:
            lastind=i+1
        else:
            print(key[i%lastind],letter,lastind)
        i+=1
    print(lastind)
    return ''.join(key[:lastind])
"""
