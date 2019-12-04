def steps_to_convert(line1, line2):
    if line1 == line2:
        return 0
    n, m = len(line1), len(line2)
    if n > m:
        line1, line2 = line2, line1
        n, m = m, n

    cur_row = range(n + 1)
    for i in range(1, m + 1):
        prev_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            if line1[j - 1] != line2[i - 1]:
                change += 1
            cur_row[j] = min(add, delete, change)

    return cur_row[n]


if __name__ == "__main__":
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
