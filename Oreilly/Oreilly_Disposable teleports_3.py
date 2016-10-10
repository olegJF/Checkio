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
    teleports_sides = sorted(teleports_string.split(','))
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
    #print('connected',connected)
    #print('one_way',one_way)
    intersection = set(connected)& set(one_way)
    if intersection:
        i=intersection.pop()
    else:
        i=connected[0]
    temp = []
    for side in teleports_sides:
        if side[0]==i:
            temp.append([i,side])
            break
        elif side[1]==i:
            temp.append([i,side])
            break
    not_cycle = []
    print('temp', temp)
    while len(set(visited_teleports))!=8:
        print('visited_teleports',visited_teleports)
        #print('countElseWay=',countElseWay(visited_teleports[-1],teleports_sides), 'visited_teleports[-1]',visited_teleports[-1])
        if len(visited_teleports)!=0:
            if countElseWay(visited_teleports[-1],teleports_sides)==0 and len(teleports)!=0:
                print('count',countElseWay(visited_teleports[-1],teleports_sides), 'visited_teleports[-1]',visited_teleports[-1])
                while countElseWay(visited_teleports[-1],teleports_sides)<2:
                    teleports.append(visited_teleports[-1])
                    teleports_sides.append(visited_teleports[-1]+visited_teleports[-2])
                    not_cycle.append(visited_teleports[-1])
                    visited_teleports.pop()
                
        if len(temp)!=0:
            num_teleport,side = temp.pop()
        else:
            num_teleport,side = getTeleport(visited_teleports[-1],teleports_sides)
        port = num_teleport
        if getTeleport(port,teleports_sides):
            
            print('Looking for num_teleport=',num_teleport,'side=',side)
            teleports_sides.remove(side)
            visited_teleports.append(num_teleport)
            if num_teleport in teleports:
                teleports.remove(num_teleport)
            if countElseWay(num_teleport,teleports_sides)>1:
                tops = []
                tops = getTopOfTriangle(num_teleport, teleports_sides)
                if '1' in tops and len(tops)>1:# Если у порта есть другие связи кроме 1-го
                    tops.remove('1')
                    if tops[0]+num_teleport in teleports_sides:
                        temp.append([tops[0],tops[0]+num_teleport])
                        
                    elif num_teleport+tops[0] in teleports_sides:
                        temp.append([tops[0],num_teleport+tops[0]])
                else:
                    intersection = set(tops)& set(one_way)
                    if len(not_cycle)!= 0:
                        intersection = set(intersection)- set(not_cycle)
                        not_cycle = []
                    no_connected = set(tops)- set(connected)
                    #print('no_connected',no_connected,'tops',tops,'intersection',intersection)
                    if intersection:# Если у порта есть соседи с одним выходом
                        i=intersection.pop()
                    elif no_connected:# Если у порта есть соседи, не соединенные с 1-м
                        i = no_connected.pop()
                    elif len(tops)>2:#
                        i = tops[0]
                    else:
                        not_visited = set(tops)& set(teleports)
                        i = not_visited.pop()
                    #print('i=',i)
                    #visited_teleports.append(i)
                    if i+num_teleport in teleports_sides:
                        temp.append([i,i+num_teleport])
                        #teleports_sides.remove(i+num_teleport)
                    elif num_teleport+i in teleports_sides:
                        temp.append([i,num_teleport+i])
                        #teleports_sides.remove(num_teleport+i)
                #print('after', visited_teleports, 'temp',temp)
                
                    
                        
            else:
                if num_teleport !=1 and num_teleport in connected:
                    connected.remove(num_teleport)
                
        else:
            visited_teleports.pop()
        #print(visited_teleports)
        #print(teleports_sides)
        
    
        
    return ''.join(visited_teleports)+'1'


print(checkio("13,14,34,32,35,52,37,38,78,16,26"))
#13,14,23,25,34,35,47,56,58,76,68
#13,14,34,32,35,52,37,38,78,16,26
#12,28,87,71,13,14,34,35,45,46,63,65
#6 12,17,87,86,85,82,65,43,35,46
#7 13,14,34,32,35,52,37,38,78,16,26



