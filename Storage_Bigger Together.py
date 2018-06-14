# -*- coding: utf-8 -*-

def bigger_together(some_list):
    import itertools
    tmp = [str(i) for i in some_list]
    length = len(tmp)
    all_var = [int(''.join(x)) for x in itertools.permutations(tmp, length)]

    return max(all_var)-min(all_var)


TESTS = [  
        {
            "input": [1,2,3,4],
            "answer": 3087,
            "explanation": "4321 - 1234 = 3087"
        },
        {
            "input": [1,2,3,4, 11, 12],
            "answer": 32099877,
            "explanation": "43212111 - 11112234 = 32099877"
        },
        {
            "input": [0, 1],
            "answer": 9,
            "explanation": "10 - 01 = 9"
        },
        {
            "input": [100],
            "answer": 0,
            "explanation": "100 - 100 = 0"
        },
        {
            "input": [3, 4],
            "answer": 9,
            "explanation": "43 - 34 = 9"
        },{
            "input": [3, 12, 22, 32],
            "answer": 2099889,
            "explanation": "3322212 - 1222323 = 2099889"
        },{
            # From http://www.shiftedup.com/2015/05/08/solution-to-problem-4
            # Helps fail wrong padding solutions.
            "input": [420, 42, 423],
            "answer": 381078,
            "explanation": "42423420 - 42042342"
        },{
            "input": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "answer": 977530864311,
            "explanation": "987654321100 - 010123456789"
        },{
            "input": [31, 3132],
            "answer": 99,
            "explanation": "313231 - 313132"
        }
    
    ]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        def test_matrix(self):
            for t in TESTS:
                matrix = t['input']
                res = bigger_together(matrix)
                answer = t['answer']
                print('answer', t['answer'])
                self.assertEqual(res, answer )
    unittest.main()




