def to_encrypt(text, delta):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if delta < 0:
        delta = delta + 26
    encrypt_str = ''
    for char in text:
        i = alphabet.find(char)
        if i == -1:
            encrypt_str += char
            continue
        tmp = i + delta
        if tmp > 26:
            i = tmp % 26
        else:
            i = tmp
        encrypt_str += alphabet[i]
    return encrypt_str

TESTS = [
        {
            "input": ["a b c", 3],
            "answer": "d e f"
        },
        {
            "input": ["a b c", -3],
            "answer": "x y z"
        },
        {
            "input": ["simple text", 16],
            "answer": "iycfbu junj"
        },
        {
            "input": ["important text", 10],
            "answer": "swzybdkxd dohd"
        },
        {
            "input": ["state secret", -13],
            "answer": "fgngr frperg"
        }
]

if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_encrypt(self):
            for t in TESTS:
                text, delta = t['input']
                res = to_encrypt(text, delta)
                answer = t['answer']
                # print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()