def to_camel_case(name):
    answer = ''
    for word in name.split('_'):
       answer += word.capitalize()
    return answer

TESTS = [
        {
            "input": "my_function_name",
            "answer": "MyFunctionName"
        },
        {
            "input": "i_phone",
            "answer": "IPhone"
        },
        {
            "input": "this_function_is_empty",
            "answer": "ThisFunctionIsEmpty"
        },
        {
            "input": "name",
            "answer": "Name"
        },
        {
            "input": "this_is_really_very_long_string",
            "answer": "ThisIsReallyVeryLongString"
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_string(self):
            for t in TESTS:
                line = t['input']
                res = to_camel_case(line)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()


# Интересные решения.
def to_camel_case_(name):

    return ''.join(map(lambda x: x.capitalize(), name.split('_')))
    


_to_camel_case = lambda x: "".join(i.title() for i in x.split('_'))



