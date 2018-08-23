month = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def date_time(time_str: str) -> str:
    date, time = time_str.split(' ')
    date_list = date.split('.')
    answer = str(int(date_list[0])) + ' ' + month[int(date_list[1])] + ' ' + date_list[2] + ' year '
    times = time.split(':')
    hours, minutes = int(times[0]), int(times[1])
    if hours == 1:
        answer += str(hours) +  ' hour '
    else:
        answer += str(hours) +  ' hours '
    if minutes == 1:
        answer += str(minutes) +  ' minute'
    else:
        answer += str(minutes) +  ' minutes'
    return answer


TESTS = [
        {
            "input": "01.01.2000 00:00",
            "answer": "1 January 2000 year 0 hours 0 minutes"
        },
        {
            "input": "09.05.1945 06:30",
            "answer": "9 May 1945 year 6 hours 30 minutes"
        },
        {
            "input": "20.11.1990 03:55",
            "answer": "20 November 1990 year 3 hours 55 minutes"
        },
        {
            "input": "09.07.1995 16:50",
            "answer": "9 July 1995 year 16 hours 50 minutes"
        },
        {
            "input": "11.04.1812 01:01",
            "answer": "11 April 1812 year 1 hour 1 minute"
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_clock(self):
            for t in TESTS:
                line = t['input']
                res = date_time(line)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()