# -*- coding: utf-8 -*-

import copy
def rotateMatrix(matrix):
    tmp = copy.deepcopy(matrix)
    for i in range(4):
        for x in range(4):
            tmp[x][3-i] = matrix[i][x]
    return tmp

def getWord(matrix, table):
    word = ''
    for i in range(4):
        if 'X' in matrix[i]:
            for y in range(4):
                if matrix[i][y]=='X':
                    word +=table[i][y]
    return word

def recall_password(array, table):
    matrix = []
    for line in array:
        tmp = []
        for i in line: tmp.append(i)
        matrix.append(tmp)
    secret_word = getWord(matrix, table)
    for i in range(3):
        matrix = copy.deepcopy(rotateMatrix(matrix))
        secret_word += getWord(matrix, table)

    return secret_word

print(recall_password(('X...','..X.','X..X','....'),
                      ('itdf','gdce','aton','qrdi')))
