# -*- coding: utf-8 -*-

def checkio(num):
    res = []
    crat = ['2','4','6','8']
    any_way = True
    not_end_yet = True
    result = 0
    tmp_array = []
    while any_way and not_end_yet:
        if str(num)[-1]=='0' or str(num)[-1]=='5':
            
            res.append(5)
            num = int(num/5)
        elif num%9==0:
            res.append(9)
            num = int(num/9)
        elif num%8==0:
            res.append(8)
            num = int(num/8)
        elif num%7==0:
            res.append(7)
            num = int(num/7)
        elif num%6==0:
            res.append(6)
            num = int(num/6)
        elif num%4==0:
            res.append(4)
            num = int(num/4)
        elif num%3==0:
            res.append(3)
            num = int(num/3)
            
        elif num%2==0:
            res.append(2)
            num = int(num/2)
        
        
        else:
            any_way = False
        if num<10:
            res.append(num)
            not_end_yet = False
    print('res',res)
    if num>9: return 0
    else:
        res = sorted(res)
        """
        while res[0]*res[1]<10:
            tmp = 1
            tmp_array = res[:]
            for dgt in res:
                if tmp*dgt<10:
                    tmp *=dgt
                    tmp_array.remove(dgt)
            res = tmp_array[:]
            res.append(tmp)
            res = sorted(res)
        """
        
        x = len(res)-1
        for i in range(len(res)):
            result +=res[i]*10**(x-i)
    return result
    
    



print(checkio(9000))
"""
while res[0]*res[1]<10:
            tmp = 1
            tmp_array = res[:]
            for dgt in res:
                if tmp*dgt<10:
                    tmp *=dgt
                    tmp_array.remove(dgt)
            res = tmp_array[:]
            res.append(tmp)
            res = sorted(res)

while res[0]*res[1]<10:
            tmp = 1
            for dgt in res:
                if tmp*dgt<10:
                    tmp *=dgt
                    
            del res[0]
            del res[0]
            res.append(tmp)
            res = sorted(res)


            """
