# -*- coding: utf-8 -*-

def relations(rings):
    numbers =set()
    for pair in rings:
        numbers.update(set(pair))
    count_intersection = [0 for i in range(max(numbers)+1)]
    for pair in rings:
        count_intersection[pair[0]] +=1
        count_intersection[pair[1]] +=1

    #print('max_intersection',max_intersection)
    return count_intersection

def break_rings1(array):
    rings = []
    for pair in array:
        rings.append(list(pair))
    begin_intersection = relations(rings)
    #print('begin_intersection',begin_intersection)
    broken_rings = max(max(rings))
    #print(broken_rings)
    max_intersection = max(begin_intersection)
    #print('max_intersection',max_intersection)
    for dgt in range(2,(max_intersection+1)):
        #print('dgt', dgt)
        copy_rings = rings[:]
        broken = 0
        while copy_rings:
            
            #print(copy_rings)
            intersection = relations(copy_rings)
            number_of_ring = intersection.index(max(intersection))
            #print(intersection)
            #print('min', min(intersection))
            if dgt in intersection and dgt in begin_intersection:
                for i in range(0,len(intersection)):
                    if intersection[i]==dgt and begin_intersection[i]==dgt:
                        #print('i', i)
                        number_of_ring = i
            #else:
                #print('max(intersection)=',max(intersection))
                #number_of_ring = intersection.index(max(intersection))
            
            #print('number_of_ring', number_of_ring)
            tmp = copy_rings[:]
            for pair in tmp:
                if number_of_ring in pair:
                    copy_rings.remove(pair)
            broken +=1
        #print(broken)
        if broken_rings > broken: broken_rings = broken
    #print(broken_rings)
    return broken_rings




import itertools
def break_rings(rings):
    nums = set(r for ring_pair in rings for r in ring_pair)#создается массив используемых цифр
    print(nums)
    for i in range(len(nums)):
        print(i)
        for comb in itertools.combinations(nums, i):
            #создаются все возможные комбинации цифр с длинной от 0 до i
            if all(any(r in comb for r in ring_pair) for ring_pair in rings):
                # для каждой комбинации цифр 
                # проверяется есть ли все эти цифры в парах
                #([1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [8, 7],
                # [8, 9], [9, 7], [10, 4], [10, 11], [11, 12], [12, 13], [12, 14])
                # т.е. как минимум одна из цифр в паре связей должна быть в комбинации
                # comb (1, 3, 5, 7, 8, 10, 12)
                # так в паре [1, 2] - есть 1, в паре [2, 3] есть 3, в паре [3, 4] - есть тоже 3...
                # каждый раз any() создаёт массив длинной, равной длине сиска связей,
                # со значением True вместо пары, если одна из цифр пары есть в комбинации,
                # и False, если ни одной из цифр нет в комбинациии.
                # после этого, эта последовательность проверяется функцией all()
                # как только все значения последовательности = True,
                # то возвращается номер иттерации,
                # который и соответствует количеству разбитых колец,
                # а массив comb и есть тот набор колец, которые нужно разбить
                # поскольку комбинация создается по нарастающей, то таким
                # образом, получается минимально необходимое кол-во колец 
                # которое нужно разбить
                #
                return i

print(break_rings(([1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [8, 7], [8, 9], [9, 7],
                      [10, 4], [10, 11], [11, 12], [12, 13], [12, 14])))

