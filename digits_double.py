
def is_one_char_difference(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n

    cur_row = range(n + 1)
    for i in range(1, m + 1):
        prev_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            if str1[j - 1] != str2[i - 1]:
                change += 1
            cur_row[j] = min(add, delete, change)
    if cur_row[n] == 1:
        return str2
    return None


def checkio(numbers):
    numbers = [str(i) for i in numbers]
    first = numbers[0]
    result = []
    stack = [[numbers.pop()]]
    while stack:
        tmp_list = stack.pop()
        str1 = tmp_list[-1]
        for i in numbers:
            res = is_one_char_difference(str1, i)
            if res:
                if res not in tmp_list:
                    tmp = tmp_list + [res]
                    stack.append(tmp)
                    if tmp[-1] == first:
                        result.append(tmp)

    min_len = min([len(i) for i in result])
    for seq in result:
        if len(seq) == min_len:
            return [int(i) for i in reversed(seq)]
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
