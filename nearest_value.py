def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    values = sorted(list(values))
    min_v = None
    max_v = None
    for i in values:
        if min_v and max_v:
            break
        if i < one:
            min_v = i
        elif i > one:
            if max_v:
                break
            max_v = i
    print(min_v, max_v)
    if not max_v:
        return min_v
    if not min_v:
        return max_v
    
    return min_v if one - min_v <= max_v - one else max_v


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
