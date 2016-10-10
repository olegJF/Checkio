# -*- coding: utf-8 -*-
OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation==OPERATION_NAMES[0]:
        if x==1 and y==1: return 1
        return 0
    elif operation==OPERATION_NAMES[1]:
        if x==1 or y==1: return 1
        return 0
    elif operation==OPERATION_NAMES[2]:
        if x==1 and y==0: return 0
        return 1
    elif operation==OPERATION_NAMES[3]:
        if x==1 and y==0 or x==0 and y==1: return 1
        return 0 
    elif operation==OPERATION_NAMES[4]:
        if x==0 and y==0 or x==1 and y==1: return 1
        return 0 
    

print(boolean(0, 1, "equivalence"))
