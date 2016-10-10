# -*- coding: utf-8 -*-
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    unit = 0
    last = 0
    while abs(number)>=base and unit<len(powers)-1:
        last = number%base
        number = number/base
        unit +=1
    number = float(number)  
    if decimals!=0:
        last = int(last) 
        if len(str(last))<decimals:
            number = str(number)
            last = str(last)
            while len(str(last))<decimals:
                number +='0'
                last+='0'
                print('number',number,'last',last)
        else: number = round(number,decimals)
    else: number = int(number)
    return str(number)+powers[unit]+suffix
    
    
        
    
    

print(friendly_number(10**32))
