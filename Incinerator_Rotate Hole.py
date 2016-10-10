# -*- coding: utf-8 -*-

def oneStepToTheRight(array):
    array.insert(0,array[-1])
    del array[-1]
    return array

def isWork(state, pipe_numbers):
    for y in pipe_numbers:
        if state[y] == 0:
            return False
    return True

def rotate(state, pipe_numbers):
    pipe_numbers = set(pipe_numbers)
    result = []
    i = 0
    while i < len(state):
        #print(state)
        if isWork(state, pipe_numbers):
            result.append(i)
        oneStepToTheRight(state)
        i +=1
    return result
print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]))



