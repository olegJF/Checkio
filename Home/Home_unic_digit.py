# -*- coding: utf-8 -*-
checkio=[1, 2, 3, 1, 3]
temp=[]
for i in checkio:
    if checkio.count(i)>1:
        temp.append(i)
        #print i
print (temp)
