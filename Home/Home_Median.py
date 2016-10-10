# -*- coding: utf-8 -*-
data=[1,10,2,9,3,8,4,7,5,6]
temp=sorted(data)
if len(temp)%2==0:
    x=len(temp)//2
    median=(temp[x-1]+temp[x])/2
else:
    median=temp[len(temp)//2]
print(temp)
print(median)
