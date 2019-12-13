def create_intervals(data):
    res = []
    tmp = []
    data = sorted(list(data))
    for i in range(len(data)):
        if not tmp:
            tmp.append(data[i])
        if i == len(data) - 1:
            tmp.append(data[i])
            res.append(tuple(tmp))
            break
        if data[i] + 1 != data[i+1]:
            tmp.append(data[i])
            res.append(tuple(tmp))
            tmp = []

    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
