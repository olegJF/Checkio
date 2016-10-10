# -*- coding: utf-8 -*-
def getTopOfTriangle(port, teleports_sides):
    tops = []
    for side in teleports_sides:
        if side[0]==port:
             tops.append(side[1])
        if side[1]==port:
             tops.append(side[0])    
    #print('tops=', tops)
    return tops


def checkio(teleports_string):  # DFS
    teleports_sides = set(teleports_string.split(','))
    goal = set("12345678")
    visited = set('1')
    queue = ['1']
    path = ''
    while len(queue)!=0:
        #print (visited)
        tops = []
        tops = getTopOfTriangle(queue[0], teleports_sides)
        for i in tops:
            if i not in visited:
                queue.append(i)
                visited.add(i)
        path +=queue[0]
        print('queue=',queue)
        del queue[0]
        print('path=',path)

        
    return path
        
        


print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))



