# -*- coding: utf-8 -*-

def checkio(matrix):
    
    import copy
    import math
    
    def findD(m):
        a = m[0][0]*m[1][1]*m[2][2]
        b = m[2][0]*m[0][1]*m[1][2]
        c = m[1][0]*m[2][1]*m[0][2]
        d = m[2][0]*m[1][1]*m[0][2]
        e = m[0][0]*m[2][1]*m[1][2]
        f = m[1][0]*m[0][1]*m[2][2]
        return a+b+c-d-e-f
    array = [[matrix[i][y] for i in range(3)] for y in range(3)]
    #print(array)
    res = [0, 225, 315]
    D = []
    D.append(findD(array))
    #print('d', D, matrix)
    for i in range(0,3):
        tmp = []
        for y in range(0,3):
            arr = copy.deepcopy(array[y])
            arr[i] = res[y]
            tmp.append(arr)
        #print('i',i, '===',tmp)
        D.append(findD(tmp))
    print('d=', D)
    result = [0,0,0]
    result[0] = D[1]/D[0]
    result[1] = D[2]/D[0]
    result[2] = D[3]/D[0]
    for i, val in enumerate(result):
        if val%1 >0:
            if val%1 >= 0.5:
                result[i] = math.ceil(val)
            elif val%1 < 0.5:
                result[i] = math.floor(val)
        result[i] = int(result[i])%360
    
            
    for i, val in enumerate(result):
        if val > 180:
            result[i] = val-360
            

    return result

##print(checkio([[1, 2, 3],
##                     [3, 1, 2],
##                     [2, 3, 1]]))


TESTS = [
        {
            "input": [
                [1, 2, 3],
                [3, 1, 2],
                [2, 3, 1]]
        },
        {
            "input": [
                [1, 4, 2],
                [2, 1, 2],
                [2, 2, 1]]
        },
        {
            "input": [
                [1, 2, 5],
                [2, 1, 1],
                [2, 5, 1]]
        },
        {
            "input": [
                [1, 3, 5],
                [3, 1, 5],
                [2, 5, 1]]
        },
        {
            "input": [
                [1, 5, 2],
                [2, 1, 7],
                [1, 3, 1]]
        },
        {
            "input": [
                [1, 3, 4],
                [2, 1, 3],
                [4, 2, 1]]
        },
        {
            "input": [
                [1, 3, 2],
                [2, 1, 3],
                [3, 2, 1]]
        },


       ]

if __name__ == "__main__":
    import unittest
    res = [0, 225, 315]

    class PaternTestCase(unittest.TestCase):
        def test_matrix(self):
            for t in TESTS:
                matrix = t['input']
                f,s,t = checkio(matrix)
                print('f,s,t', f,s,t)
                temp = [0, 0, 0]
                temp[0] += f
                temp[1] += matrix[0][1] * f
                temp[2] += matrix[0][2] * f

                temp[0] += matrix[1][0] * s
                temp[1] += s
                temp[2] += matrix[1][2] * s

                temp[0] += matrix[2][0] * t
                temp[1] += matrix[2][1] * t
                temp[2] += t
                #print(temp)
                temp = [n % 360 for n in temp]
                #print(temp)
                self.assertEqual(temp, res)
    unittest.main()
