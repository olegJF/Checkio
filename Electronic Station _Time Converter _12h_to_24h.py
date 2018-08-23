def time_converter(t):
    import time
    
    return time.strftime('%H:%M', time.strptime(t.replace('.', ''), '%I:%M %p'))


TESTS = [
        {
            "input": '12:30 p.m.',
            "answer": '12:30'
        },
        {
            "input": '9:00 a.m.',
            "answer": '09:00'
        },
        {
            "input": '11:15 p.m.',
            "answer": '23:15'
        },
        {
            "input": '6:50 p.m.',
            "answer": '18:50'
        },
        {
            "input": '7:07 a.m.',
            "answer": '07:07'
        },
        {
            "input": '12:00 a.m.',
            "answer": '00:00'
        },
        {
            "input": '12:00 p.m.',
            "answer": '12:00'
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_clock(self):
            for t in TESTS:
                line = t['input']
                res = time_converter(line)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()