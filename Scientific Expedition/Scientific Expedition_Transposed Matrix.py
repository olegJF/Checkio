# -*- coding: utf-8 -*-
def checkio(data):
    result = [[0 for y in range(len(data))]for x in range(len(data[0]))]
    i = 0
    for row in data:
        y = 0
        for item in row:
            result[y][i] = item
            y +=1
        i +=1
    return result
    

print(checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]))
