# -*- coding: utf-8 -*-
data=([

    "X.O",

    "XX.",

    "OO."])
def checkio(data):
    diagonal_1=''
    for i in range(0,3):
        col =data[0][i]+data[1][i]+data[2][i]
        diagonal_1+=data[i][i]
        data.append(col)
    data.append(diagonal_1)
    diagonal_2=data[0][2]+data[1][1]+data[2][0]
    data.append(diagonal_2)
    print(data)
    for row in data:
        if row.count('X')==3:
            return 'X'
        elif row.count('O')==3:
            return 'O'
    return 'D'

print(checkio(data))


