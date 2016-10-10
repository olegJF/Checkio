# -*- coding: utf-8 -*-

            
def checkio(number):
    from math import sqrt
    num = int(sqrt(number*2))
    triangular_numbers = [int(i*(i+1)/2) for i in range(num)]
    result = []
    result.append(triangular_numbers[-1])
    tmp = triangular_numbers[-1]
    for i in range(len(triangular_numbers)-2,0, -1):
        print('i=',i,'rusult=',result, 'tmp=',tmp)
        if tmp+triangular_numbers[i]>number and len(result)<2:
            tmp = triangular_numbers[i]
            result.pop()
            result.append(triangular_numbers[i])
            print('new')
        else:
            if tmp == number:
                break
            elif tmp+triangular_numbers[i]<=number:
                tmp += triangular_numbers[i]
                result.append(triangular_numbers[i])
            elif tmp+triangular_numbers[i]>number and len(result)!=0:
                tmp -= triangular_numbers[0]
                del result[0]
            
        
        
    
    
    return result



print(checkio(64))
