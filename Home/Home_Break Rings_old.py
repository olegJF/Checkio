# -*- coding: utf-8 -*-

def relations(rings):
    numbers =set()
    for pair in rings:
        numbers.update(set(pair))
    max_intersection = [0 for i in range(max(numbers)+1)]
    for pair in rings:
        max_intersection[pair[0]] +=1
        max_intersection[pair[1]] +=1

    #print('max_intersection',max_intersection)
    return max_intersection.index(max(max_intersection)), max_intersection

def break_rings(array):
    rings = []
    for pair in array:
        rings.append(list(pair))
    max_numbers=[]
    _, tmp = relations(rings)
    max_number = max(tmp)
    broken_rings = []
    for dgt in range(1,len(tmp)):
        #print(dgt)
        copy_rings = rings[:]
        broken = 0
        while copy_rings:
            #print(rings)
            if broken == 0: max_number=dgt
            else: max_number, _ = relations(copy_rings)
            #print('max_number', max_number)
            tmp = copy_rings[:]
            for pair in tmp:
                if max_number in pair:
                    copy_rings.remove(pair)
            broken +=1
        broken_rings.append(broken)
    print(broken_rings)
    return min(broken_rings)

print(break_rings(([1, 2], [2, 3], [3, 4], [4, 5], [5, 2],
                      [1, 6], [6, 7], [7, 8], [8, 9], [9, 6],
                      [1, 10], [10, 11], [11, 12], [12, 13], [13, 10],
                      [1, 14], [14, 15], [15, 16], [16, 17], [17, 14])))


