def all_the_same(elements):
    tmp = len(set(elements))
    return any((tmp == 0 , tmp == 1))

TESTS = [
        {
            "input": [1, 1, 1],
            "answer": True
        },
        {
            "input": [1, 2, 1],
            "answer": False
        },
        {
            "input": [],
            "answer": True,
            "explanation": "All elements in empty list are equal"
        },
        {
            "input": [1],
            "answer": True,
            "explanation": "List contains only one element."
        },
    
        {
            "input": [1, 'a', 1],
            "answer": False
        },
        {
            "input": [600000],
            "answer": True
        },
        {
            "input": [10000, 99999],
            "answer": False
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_morse(self):
            for t in TESTS:
                some_list = t['input']
                res = all_the_same(some_list)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()