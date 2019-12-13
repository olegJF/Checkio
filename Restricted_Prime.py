# math = __builtins__['__i' 'm' 'p' 'o' 'r' 't__']('math')
# operator = __builtins__['__i' 'm' 'p' 'o' 'r' 't__']('operator')

get_module = getattr(__builtins__, ''.join(['__i', 'm', 'p', 'o', 'r', 't__']))
operator = get_module('operator')
math = get_module('math')


def checkio(dgt):
    sq = int(math.sqrt(dgt))
    dgts = []
    i = int(True) + int(True)
    while i <= sq:
        dgts.append(i)
        i += int(True)
    for x in dgts:
        if not operator.mod(dgt, x):
            return False
    return True

if __name__ == "__main__":
    assert checkio(5) == True
    assert checkio(18) == False
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
    for p in primes:
        assert checkio(p) == True
    print('OK')

