# -*- coding: utf-8 -*-
def checkio(number):
    from math import sqrt
    num = int(sqrt(number*2))
    triangular_numbers = [int(i*(i+1)/2) for i in range(num)]
    result = []
    tmp = 0
    for i in triangular_numbers:
        tmp +=i
        if i!=0: result.append(i)
        if tmp == number:
            break
        print('i=',i,'rusult=',result, 'tmp=',tmp)
        if tmp+i>number:
            while tmp+i>number:
                if tmp == number:
                    break
                print('while i=',i,'rusult=',result, 'tmp=',tmp)
                tmp -=result[0]
                del result[0]
            if tmp == number:
                break
    return result



print(checkio(216))
