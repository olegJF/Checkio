# -*- coding: utf-8 -*-

def checkio(land_map):
    row = len(land_map)
    column = len(land_map[0])
    res = []
    for i in range(row):
        for j in range(column):
            if land_map[i][j] == 1:
                island = []
                island.append((i, j))
                for x,y in island:
                    #print('island=',island)
                    if column == 1:
                        if x == row-1: borders = []
                        else: borders = [(x+1,0)]
                    elif row == 1:
                        if y == column-1: borders = []
                        else: borders = [(0,y+1)]
                    else:    
                        if x ==0 and y == 0:
                            borders = [(0,1), (1,0), (1,1)]
                        elif x ==0 and y == column-1:
                            borders = [(0,y-1),(1,y-1), (1,y)]
                        elif x == row-1 and y == 0:
                            borders = [(x,y+1)]
                        elif x == row-1 and y == column-1:
                            iborders = [(x,y-1)]
                        elif y == 0:
                            borders = [(x,y+1), (x+1,y), (x+1,y+1)]
                        elif y == column-1:
                            borders = [(x,y-1), (x+1,y-1), (x+1,y)]
                        elif x == row-1 and y != column-1:
                            borders = [(x,y-1), (x,y+1)]
                        elif x == 0:
                            borders = [(x,y-1), (x,y+1), (x+1, y-1), (x+1, y),(x+1,y+1)]
                        else:
                            borders = [(x,y-1), (x,y+1), (x-1,y+1), (x+1, y-1), (x+1, y),(x+1,y+1)]
                    #print('x,y=',x,y,'borders=',borders)
                    for border in borders:
                        a,b = border
                        #print('a,b=',a,b)
                        if land_map[a][b] == 1:
                            if (a, b) not in island:
                                island.append((a, b))
                                #print('a,b=',a,b)
                res.append(len(island))
                for x,y in island:
                    land_map[x][y] = 0
                #print('land_map',land_map)

    return sorted(res)

##print(checkio([ [1, 1, 1, 1, 1],
##                [1, 1, 1, 1, 1],
##                [1, 1, 0, 1, 1],
##                [1, 1, 1, 1, 1],
##                [1, 1, 1, 1, 1]]))


TESTS = [
        {
            "input": [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]],
            "answer": [1, 3],
            "explanation": [[1, 3, 1], [3, 1.5, 2.5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 0, 0]],
            "answer": [5],
            "explanation": [[5, 2.5, 2.5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]],
            "answer": [2, 3, 3, 4],
            "explanation": [[2, 1.5, 0], [3, 1, 4], [3, 3, 3], [4, 5, 2.5]]
        },
        {
            "input": [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]],
            "answer": [24],
            "explanation": [[24, 0.5, 2]]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 1],
                [1, 0, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1]],
            "answer": [4, 20],
            "explanation": [[4, 2.5, 2.5], [20, 0, 2.5]]
        },
        {
            "input": [
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0]
            ],
            "answer": [5, 6, 7],
            "explanation": [[5, 2, 1], [6, 2.5, 3], [7, 3, 5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0]
            ],
            "answer": [2, 5, 8],
            "explanation": [[2, 5.5, 1], [5, 6, 4], [8, 1, 2]]
        },
        {
            "input": [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]

            ],
            "answer": [1],
            "explanation": [[1, 1, 1]]
        },
        {
            "input": [
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]
            ],
            "answer": [16],
            "explanation": [[16, 1.5, 1.5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
            "answer": [3, 4],
            "explanation": [[3, 1.5, 2.5], [4, 3.5, 0.5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0]],
            "answer": [6],
            "explanation": [[6, 2.5, 2.5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]],
            "answer": [2, 3, 3, 3],
            "explanation": [[2, 1.5, 0], [3, 1, 4], [3, 3, 3], [3, 5, 3]]
        },
        {
            "input": [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1]],
            "answer": [23],
            "explanation": [[23, 0.5, 2]]
        },
        {
            "input": [
                [1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1]],
            "answer": [3, 20],
            "explanation": [[3, 2.5, 2.5], [20, 0, 2.5]]
        },
        {
            "input": [
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0]
            ],
            "answer": [4, 6, 7],
            "explanation": [[4, 1.5, 1], [6, 2.5, 3], [7, 3, 5]]
        },
        {
            "input": [
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0]
            ],
            "answer": [2, 5, 7],
            "explanation": [[2, 5.5, 1], [5, 6, 4], [7, 1, 2]]
        },
        {
            "input": [
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 0]

            ],
            "answer": [1],
            "explanation": [[1, 0, 1]]
        },
        {
            "input": [
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]
            ],
            "answer": [20],
            "explanation": [[20, 2, 1.5]]
        },
        {
            "input": [
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
            ],
            "answer": [1, 1, 1, 1, 16],
            "explanation": [[1, 0, 0],
                            [1, 8, 0],
                            [1, 0, 8],
                            [1, 8, 8],
                            [16, 2, 4]]
        },
        {
            "input": [
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
            ],
            "answer": [9],
            "explanation": [[9, 4, 0]]
        },
        {
            "input": [[1, 1, 1, 1, 0, 1, 1, 1, 1]],
            "answer": [4, 4],
            "explanation": [
                [4, 0, 1.5],
                [4, 0, 6.5]
            ]
        },
        {
            "input": [
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
            ],
            "answer": [17],
            "explanation": [[17, 4, 4]]
        },
        {
            "input": [
                [1]
            ],
            "answer": [1],
            "explanation": [[1, 0, 0]]
        },


      ]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        def test_matrix(self):
            for t in TESTS:
                matrix = t['input']
                res = checkio(matrix)
                answer = t['answer']
                print('answer', t['answer'])
                self.assertEqual(res, answer )
    unittest.main()




