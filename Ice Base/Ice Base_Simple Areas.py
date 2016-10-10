# -*- coding: utf-8 -*-

def simple_areas(*args):
    from math import sqrt, pi
    sides = list(args)
    size = len(sides)
    if size == 1: return round((pi*sides[0]**2)/4,2)
    elif size == 2: return sides[0]*sides[1]
    p = sum(sides)/2
    return sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

print(simple_areas(3,5,4))
