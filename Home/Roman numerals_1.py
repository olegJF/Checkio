# -*- coding: utf-8 -*-
def checkio(num):

    result= []

    romans= ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')

    nums= (1000,900,500,400,100,90,50,40,10,9,5,4,1)

    table= zip(nums,romans)
    #print(table)

    for n,r in table:
        print('n=',n,'r=',r)

        while num >= n:

            result.append(r)
            print('result=',result,'num=',num)

            num -= n

    return ''.join(result)


    

print(checkio(88))
