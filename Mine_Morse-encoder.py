MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.',
         ' ': ' '
        }

def morse_encoder(text):
    morse = ''
    text = text.lower()
    for chr in text:
        morse += MORSE[chr] + ' '
        
    return morse.strip()






TESTS = [

            {
                "input": "some text",
                "answer": "... --- -- .   - . -..- -"
            },
            {
                "input": "I was born in 1990",
                "answer": "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
            },
            {
                "input": "abcdefghijklmnopqrstuvwxyz",
                "answer": ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
            },
            {
                "input": "0123456789 are digits",
                "answer": "----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ..."
            },
            {
                "input": "v3ry 10ng str1ng w1th s0m3 numb3r5",
                "answer": "...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .---- - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. ....."
            }

        ]
        
if __name__ == "__main__":
    import unittest
    
    class PaternTestCase(unittest.TestCase):
        
        def test_morse(self):
            for t in TESTS:
                text = t['input']
                res = morse_encoder(text)
                answer = t['answer']
                print(len(res), len(t['answer']))
                self.assertEqual(res, answer )
    unittest.main()