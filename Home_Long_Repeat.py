def long_repeat(line):
    chars = set(line)
    print(chars)
    max_len = 0
    for chr in chars:
        tmp_len = 0
        tmp_str = chr
        while line.find(tmp_str) != -1:
            tmp_len += 1
            tmp_str += chr
        if tmp_len > max_len:
            max_len = tmp_len
    return max_len



TESTS = [
        {
            "input": "sdsffffse",
            "answer": 4
        },
        {
            "input": "ddvvrwwwrggg",
            "answer": 3
        },
        {
            "input": "",
            "answer": 0
        },{
            "input": "abababaab",
            "answer": 2
        },{
            "input": "abababa",
            "answer": 1
        },{
            "input": "aa",
            "answer": 2
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_encrypt(self):
            for t in TESTS:
                line = t['input']
                res = long_repeat(line)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()