def reverse_ascending(items):
    if len(items) < 2:
        return items
    res = []
    tmp = []
    for i in range(len(items)-1):
        if items[i] >= items[i+1]:
            if i > 0 and items[i] > items[i-1]:
                tmp.append(items[i])
                tmp.reverse()
                res.extend(tmp)
                tmp = []
            else:
                res.append(items[i])
        else:
            tmp.append(items[i])
        if i == len(items)-2:
            if items[i] < items[i + 1]:
                tmp.append(items[i+1])
                tmp.reverse()
                res.extend(tmp)
                tmp = []
            else:
                res.append(items[i+1])
    if tmp:
        tmp.reverse()
        res.extend(tmp)
    return res


if __name__ == '__main__':
    print("Example:")
    # print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
