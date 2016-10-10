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
    while len(set(visited_teleports))!=8 and visited_teleports[-1] not in connected:
        print(set(visited_teleports))
        print('teleports_sides=',teleports_sides)
        if getTeleport(visited_teleports[-1],teleports_sides):
            num_teleport,side = getTeleport(visited_teleports[-1],teleports_sides)
            #print('num_teleport=',num_teleport,'side=',side)
            tops = getTopOfTriangle(num_teleport, teleports_sides)
            teleports_sides.remove(side)
            #проверить, если у телепорта есть другая связь, кроме связи с 1 портом
            if '1' in tops and len(tops)>1:
                # удалить(перенести) связь порта с 1 в другой стек
                if '1'+num_teleport in teleports_sides:
                    teleports_sides.remove('1'+num_teleport)
                elif num_teleport+'1' in teleports_sides:
                    teleports_sides.remove(num_teleport+'1')
            if num_teleport !=1 and num_teleport in connected:
                connected.remove(num_teleport)
            
            
            visited_teleports.append(num_teleport)
            print('visited_teleports=',visited_teleports)
            if num_teleport in teleports:
                teleports.remove(num_teleport)
            """
            if num_teleport not in one_way:
                print(num_teleport)
                if getTeleport(visited_teleports[-1],teleports_sides):
                    new_teleport,side = getTeleport(visited_teleports[-1],teleports_sides)
                    if new_teleport in connected and num_teleport!=1 and len(teleports)>=2:
                        print('remove',side,'not visited teleports=',teleports)
                        teleports_sides.remove(side)
            """            
                
            
            
            #if countElseWay(visited_teleports[-2],teleports_sides)>=1 and num_teleport in visited_teleports:
                #visited_teleports.pop()
                #print(num_teleport)
        else:
            visited_teleports.pop()
        #print(visited_teleports)
        #print(teleports_sides)
        
    
        
    return visited_teleports


print(checkio("13,14,23,25,34,35,47,56,58,76,68"))



