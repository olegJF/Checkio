# -*- coding: utf-8 -*-
def checkio(matrix):
    size = len(matrix)
    if not size: return False
    for i in range(size):
        for j in range(i,size):
            if i!=j:
                if -matrix[i][j]!= matrix[j][i]:
                    return False
            else:
                if matrix[i][j]!= 0:
                    return False
    
    return True

print(checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]))
    
