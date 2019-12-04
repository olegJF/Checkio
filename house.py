def house(plan):
    plan = [row for row in plan.split('\n') if row]
    min_hight, max_hight = len(plan), 0
    min_widht, max_widht = len(plan[0]), 0
    for i, row in enumerate(plan):
        if '#' in row:
            min_hight = i if i < min_hight else min_hight
            max_hight = i if i > max_hight else max_hight
            index_hash = row.find('#')
            min_widht = index_hash if index_hash < min_widht else min_widht
            while index_hash != -1:
                max_widht = index_hash if index_hash > max_widht else max_widht
                index_hash = row.find('#', index_hash + 1)
    hight = (max_hight - min_hight) + 1
    widht = (max_widht - min_widht) + 1
    return hight * widht if hight > 0 and widht > 0 else 0


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
