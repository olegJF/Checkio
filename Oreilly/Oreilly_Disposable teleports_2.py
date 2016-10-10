# -*- coding: utf-8 -*-

def getTeleport(num, array):
    for side in array:
        if side[0]==num:
             return side[1],side
        if side[1]==num:
            return side[0],side
    return False

def notEnd(teleports, num_teleport, connected):
    if len(teleports)==0 and num_teleport in connected:
        return False
    return True

def countElseWay(num, array):
    count = 0
    for side in array:
        if side[0]==num or side[1]==num:
             count +=1
        
    return count

def getTopOfTriangle(port, teleports_sides):
    tops = []
    for side in teleports_sides:
        if side[0]==port:
             tops.append(side[1])
        if side[1]==port:
             tops.append(side[0])    
    #print('tops=', tops)
    return tops
        
            
def checkio(teleports_string):
    teleports_sides = teleports_string.split(',')
    teleports = ['2','3','4','5','6','7','8']
    visited_teleports = ['1']
    connected = []
    one_way = ['1']
    for port in teleports:
        if countElseWay(port,teleports_sides)==2:
            one_way.append(port)
    print('teleports_sides=',teleports_sides)
    for side in teleports_sides:
        if side[0]=='1':
            connected.append(side[1])
        if side[1]=='1':
            connected.append(side[0])
    num_teleport = 1
    print(connected)
    print(one_way)
    temp = []
    """
    for port in one_way:
        if getTopOfTriangle(port, teleports_sides):
            tops= getTopOfTriangle(port, teleports_sides)
            print('tops=', tops)
            for i in tops:
                for j in tops:
                    if i!=j and i+j in teleports_sides:
                        teleports_sides.remove(i+j)    
            
    """
    while len(set(visited_teleports))!=8 and visited_teleports[-1]:
        #print(set(visited_teleports))
        #print('teleports_sides=',teleports_sides)
        if len(temp)!=0:
            num_teleport,side = temp.pop()
        else:
            num_teleport,side = getTeleport(visited_teleports[-1],teleports_sides)
        port = num_teleport
        if getTeleport(port,teleports_sides):
            
            print('num_teleport=',num_teleport,'side=',side)
            teleports_sides.remove(side)
            if countElseWay(num_teleport,teleports_sides)>1:
                visited_teleports.append(num_teleport)
                if num_teleport in teleports:
                    teleports.remove(num_teleport)
                if num_teleport !='1':
                    tops = []
                    tops = getTopOfTriangle(num_teleport, teleports_sides)
                    intersection = set(tops)& set(one_way)
                    no_connected = set(tops)- set(connected)
                    print('no_connected',no_connected,'tops',tops,'intersection',intersection)
                    if intersection:
                        i=intersection.pop()
                    elif no_connected:
                        i = no_connected.pop()
                    elif len(tops)>2:
                        i = tops[0]
                    else:
                        not_visited = set(tops)& set(teleports)
                        i = not_visited.pop()
                    print('i=',i)
                    #visited_teleports.append(i)
                    if i+num_teleport in teleports_sides:
                        temp.append([i,i+num_teleport])
                        #teleports_sides.remove(i+num_teleport)
                    elif num_teleport+i in teleports_sides:
                        temp.append([i,num_teleport+i])
                        #teleports_sides.remove(num_teleport+i)
                print('after', visited_teleports, 'temp',temp)
                
                    
                        
            else:
                if num_teleport !=1 and num_teleport in connected:
                    connected.remove(num_teleport)
                visited_teleports.append(num_teleport)
        else:
            visited_teleports.pop()
        #print(visited_teleports)
        #print(teleports_sides)
        
    
        
    return visited_teleports


print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))



