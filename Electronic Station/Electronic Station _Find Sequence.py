# -*- coding: utf-8 -*-
def isTrue(num, row):
    if row.count(num)>=4:
        cnt = 0
        for dgt in row:
            if dgt==num:
                cnt +=1
                if cnt>=4: return True
            else: cnt = 0
    return False

def is4InRow(num, array):
    for row in array:
        if isTrue(num, row): return True
            
    for i in range(len(array)):
        column = [row[i] for row in array]
        if isTrue(num, column): return True
            
    cnt_diagonal = len(array)-4
    size = len(array)-1
    diagonal, diagonal_obr = [], []
    
    for i in range(len(array)):
        diagonal.append(array[i][i])
        diagonal_obr.append(array[i][size-i])
    if isTrue(num, diagonal): return True
    if isTrue(num, diagonal_obr): return True
    
    if cnt_diagonal>0:
        size +=1
        for x in range(1,cnt_diagonal+1):
            z = (size-1)-x
            left, right, left_obr, right_obr = [], [], [], []
            for y in range(size-x):
                left.append(array[y+x][y])
                right.append(array[y][y+x])
                left_obr.append(array[y][z-y])
                right_obr.append(array[y+x][z-y+x])
            if isTrue(num, left) or isTrue(num, right): return True
            if isTrue(num, left_obr) or isTrue(num, right_obr): return True
        
def checkio(array):
    numbers = set()
    for i in array:
        numbers=numbers.union(set(i))
    for num in numbers:
        if is4InRow(num, array):
            return True
        
    return False
    
    



print(checkio([
    [1, 2, 1, 1, 2],
    [5, 4, 2, 1, 5],
    [3, 5, 1, 5, 3],
    [1, 7, 5, 5, 2],
    [1, 4, 2, 6, 5]
]))



def checkio(matrix, l=3):

    q = range(len(matrix))

    ls = lambda x:len(set(x))

    for i in q:

        for j in q:

            if i+l in q and ls([matrix[i+n][j] for n in range(4)])==1: return True

            if j+l in q and ls([matrix[i][j+n] for n in range(4)])==1: return True

            if j+l in q and i+l in q and ls([matrix[i+n][j+n] for n in range(4)])==1: return True

            if j-l in q and i+l in q and ls([matrix[i+n][j-n] for n in range(4)])==1: return True

    return False


