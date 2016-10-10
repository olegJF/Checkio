# -*- coding: utf-8 -*-

def count_inversion(sequence):
    inversions = 0
    for idx1, i1 in enumerate(sequence):
        print(idx1, i1)
        right = sequence[idx1:]
        inversions += sum([int(i1 > i2) for i2 in right])
           

    return inversions


    
     
    

print(count_inversion((5, 3, 2, 1, 0)))
