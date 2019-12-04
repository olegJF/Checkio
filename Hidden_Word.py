def find_word(array, word):
    res = None
    for i, row in enumerate(array):
        position = row.find(word)
        if position >= 0:
            res = (i, position)
    return res

def checkio(text, word):
    text_array = text.lower().replace(' ', '').split('\n')
    res = find_word(text_array, word)
    if res:
        row_id = res[0] + 1
        return [row_id, res[1]+1, row_id, res[1]+len(word)]
    inverted_array = []
    size = max((len(st) for st in text_array))
    for i in range(size):
        tmp = ''
        for row in text_array:
            if i < len(row):
                tmp += row[i]
            else:
                tmp += ' '
        inverted_array.append(tmp)
    res = find_word(inverted_array, word)
    if res:
        col_id = res[0] + 1
        return [res[1]+1, col_id, res[1]+len(word), col_id]
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
