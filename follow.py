def follow(instructions):
    steps = {'f': [0, 1], 'b': [0, -1], 'l': [-1, 0], 'r': [1, 0]}
    res = [0, 0]
    for step in instructions:
        res[0] += steps[step][0]
        res[1] += steps[step][1]
    return tuple(res)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
