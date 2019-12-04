from collections import Sequence
from itertools import chain, count

def depth(seq):
    for level in count():
        if not seq:
            return level
        seq = list(chain.from_iterable(s for s in seq if isinstance(s, Sequence)))
        print(seq)

def how_deep(structure):
    sizes = [1]
    for item in structure:
        stack = []
        deep = 1
        if isinstance((item), tuple):
            stack = [item]
            deep += 1
            while len(stack) > 0:
                nested = stack.pop()
                for x in nested:
                    if isinstance((x), tuple):
                        deep += 1
                        stack.append(x)
        sizes.append(deep)
    return max(sizes)


if __name__ == '__main__':
    print("Example:")
    print(depth((1,2,((3),(4)))))

    # These "asserts" are used for self-checking and not for an auto-testing
##    assert how_deep((1, 2, 3)) == 1
##    assert how_deep((1, 2, (3,))) == 2
##    assert how_deep((1, 2, (3, (4,)))) == 3
##    assert how_deep(()) == 1 #(1,2,((3),(4)))
##    assert how_deep(((),)) == 2
##    assert how_deep((((),),)) == 3
##    assert how_deep((1, (2,), (3,))) == 2
##    assert how_deep((1, ((),), (3,))) == 3 
    print("Coding complete? Click 'Check' to earn cool rewards!")
