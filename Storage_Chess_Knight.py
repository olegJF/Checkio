# -*- coding: utf-8 -*-
import copy

def chess_knight(start, moves):
    all_move = []
    horse_move = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    chr_str = '_abcdefgh'
    
    for i in range(moves):
        tmp = []
        if len(all_move) == 0:
            tmp.append(start)
            
        else:
            tmp = copy.deepcopy(all_move)
        while tmp:
            position = tmp.pop()
            chr, dgt = position[0], int(position[1])
            chr_dgt = chr_str.find(chr)
            for pair in horse_move:
                next_chr_dgt = chr_dgt + pair[0]
                next_dgt = dgt + pair[1]
                if next_chr_dgt > 8 or next_chr_dgt < 1:
                    next_chr_dgt = None
                if next_dgt > 8 or next_dgt < 1:
                    next_dgt = None
                
                if next_chr_dgt and next_dgt:
                    next_move = chr_str[next_chr_dgt] + str(next_dgt)
                    if next_move not in all_move:
                        all_move.append(next_move)
    
    return sorted(all_move)
    


TESTS = [
        {
            "input": ['a1', 1],
            "answer": ['b3', 'c2']
        },
        {
            "input": ['h8', 2],
            "answer": ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
        },
        {
            "input": ['e5', 1],
            "answer": ['c4', 'c6', 'd3', 'd7', 'f3', 'f7', 'g4', 'g6']
        }
    ]


if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        def test_matrix(self):
            for t in TESTS:
                start, moves = t['input']
                res = chess_knight(start, moves)
                answer = t['answer']
                # print('answer', t['answer'])
                self.assertEqual(res, answer )
    unittest.main()




