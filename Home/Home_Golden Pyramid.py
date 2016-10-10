# -*- coding: utf-8 -*-

def count_gold(pyramid):
    result = []
    for i in range(len(pyramid)): 
        result.append([])
        for y in range(len(pyramid[i])):
            result[i].append(0)
    result[0][0] = pyramid[0][0]
    result[1][0] = result[0][0] + pyramid[1][0]
    result[1][1] = result[0][0] + pyramid[1][1]

    for i in range(1, len(pyramid)-1):
        for y in range(len(pyramid[i])):
            left = result[i][y]+pyramid[i+1][y]
            right = result[i][y]+pyramid[i+1][y+1]
            if result[i+1][y]<left: result[i+1][y]=left
            if result[i+1][y+1]<right: result[i+1][y+1]=right


    return max(result[-1])

print(count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )))

# n = len(pyramid)
# result = [[0 for j in range(i + 1)] for i in range(n)]
