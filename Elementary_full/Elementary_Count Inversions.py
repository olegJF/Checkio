# -*- coding: utf-8 -*-

def count_inversion(sequence):
    matrix = list(sequence)
    count = 0
    if matrix == matrix.sort():
        return count, 'yes' 
    for y in range(len(matrix)-1):
        for i in range(len(matrix)-1):
            if matrix[i]>matrix[i+1]:
                matrix[i],matrix[i+1] = matrix[i+1],matrix[i]
                count +=1
    return count
    
     
    

print(count_inversion((0, 1, 2, 3)))
