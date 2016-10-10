# -*- coding: utf-8 -*-

def checkio(time):
    morse = ['....','...-','..-.','..--','.-..','.-.-','.--.','.---','-...','-..-']
    result = ''
    time = time.split(':')
    t = 0
    for part in time:
        if len(part)==1:
            part = '0'+part
        if t==0:
            result += morse[int(part[0])][2:]+' '+morse[int(part[1])]+' : '
        elif t==1:
            result += morse[int(part[0])][1:]+' '+morse[int(part[1])]+' : '
        else:
            result += morse[int(part[0])][1:]+' '+morse[int(part[1])]
        t +=1
    return result
    
        
    
    

print(checkio("0:1:2"))
