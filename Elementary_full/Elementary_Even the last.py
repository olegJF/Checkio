# -*- coding: utf-8 -*-
def checkio(array):
    if len(array)==0: return 0
    summary = 0
    for i in range(0,len(array), 2):
        summary += array[i]
    return summary*array[len(array)-1]

print(checkio([]))
