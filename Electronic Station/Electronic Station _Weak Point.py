# -*- coding: utf-8 -*-
def summ(array):
    res = 0
    for i in array: res+=i
    return res

def checkio(array):
    row,col = 0,0
    tmp=0
    for i in range(len(array)):
        if i==0: tmp=summ( array[i])
        else:
            if summ( array[i])< tmp:
                col=i
                tmp = summ( array[i])
    tmp=0
    for z in range(len(array)):
        column = [row[z] for row in array]
        if z==0: tmp=summ( column)
        else:
            if summ( column)< tmp:
                row=z
                tmp = summ(column)
    
            
    
    return [col,row]



print(checkio([[7, 2, 4, 2, 8],

            [2, 8, 1, 1, 7],

            [3, 8, 6, 2, 4],

            [2, 5, 2, 9, 1],

            [6, 6, 5, 4, 5]]))



def weak_point(matrix):

    y = [sum(row) for row in matrix]

    x = [sum(matrix[j][i] for j in range(len(matrix[i])) ) for i in range(len(matrix))]

​

    return y.index(min(y)), x.index(min(x))


def weak_point(matrix):

    x = [sum(x) for x in matrix]

    y = [sum(x) for x in zip(*matrix)]

    return x.index(min(x)), y.index(min(y))


def weak_point(matrix):

    row = list(map(sum, matrix))

    col = list(map(sum, zip(*matrix)))

    return [row.index(min(row)),col.index(min(col))]




