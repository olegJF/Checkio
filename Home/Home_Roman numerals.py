# -*- coding: utf-8 -*-
def checkio(data):
    units = ['','I','II','III','IV','V','VI','VII','VIII','IX','X']
    tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    result = ''
    if data>=1000:
        result += 'M'*(data//1000)
        data = data%1000
    if data>=100:
        result += hundreds[data//100]
        data = data%100
    if data>=10:
        result += tens[data//10]
        data = data%10
    if data>=1:
        result += units[data]
    return result
    

print(checkio(3888))
