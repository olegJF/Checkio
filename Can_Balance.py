from typing import Iterable


def can_balance(weights: Iterable) -> int:

    def is_balanced(_indx):
        data = [[reversed(weights[:_indx]), 0], [weights[_indx+1:], 0]]
        for lst in data:
            for _i, val in enumerate(lst[0]):
                lst[1] += val * (_i + 1)
        return data[0][1] == data[1][1]

    if len(weights) == 1:
        return 0
    size = len(weights) // 2

    for i in range(size):
        tmp = [is_balanced(size - i), is_balanced(size + i)]
        if any(tmp):
            return size - i if tmp[0] else size + i
    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
