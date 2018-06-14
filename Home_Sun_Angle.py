def sun_angle(time):
    time = time.split(':')
    hours, minutes = int(time[0]), int(time[1])
    if  hours < 6 or hours >= 18:
        return "I don't see the sun!"
    degree = 15*((hours-6) + (minutes/60))
    return degree


TESTS = [
        {
            "input": '07:00',
            "answer": 15
        },
        {
            "input": '12:15',
            "answer": 93.75
        },
        {
            "input": '12:30',
            "answer": 97.5
        },
        {
            "input": '05:55',
            "answer": "I don't see the sun!"
        },
        {
            "input": "18:01",
            "answer": "I don't see the sun!"
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_encrypt(self):
            for t in TESTS:
                time = t['input']
                res = sun_angle(time)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()