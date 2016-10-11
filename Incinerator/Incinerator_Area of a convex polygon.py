# -*- coding: utf-8 -*-

def checkio(data):
    sqr = 0
    for i in range(len(data)):
        if i==len(data)-1:
            sqr += (data[i][0]*data[0][1] - data[i][1]*data[0][0])
        else:
            sqr += (data[i][0]*data[i+1][1] - data[i][1]*data[i+1][0])
    return round(abs(sqr/2), 1)

print(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]))



