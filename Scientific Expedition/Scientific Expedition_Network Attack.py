# -*- coding: utf-8 -*-
def isSumZero(array):
    t = 0
    for i in array.values(): t+=i
    if t == 0: return True
    
def capture(matrix):
    time = 0
    length = len(matrix[0])
    network = {}
    for i in range(length):
        if matrix[0][i]==1 and i not in network and matrix[i][i]!=0:
            network[i] = matrix[i][i]
     
    print(network)
    while True:
        time +=1
        for key in network:
            if network[key]>0:
                network[key] -=1
                #print('time ',t)
        print('network=',network, 'after time=',time)
        
        #нужен блок проверки - если все значения ==0, тогда возврат значения t
        if 0 in network.values():
            
            temp = network.copy()
            for key in network:
                if network[key]==0:
                    for i in range(length):
                        if matrix[key][i]==1 and i not in network and matrix[i][i]!=0:
                            temp[i] = matrix[i][i]
                            #print(temp)
        
            network = temp.copy()
        if isSumZero(network): return time

        #print('t',t)

    #return network
        
        
 
    
        
    
    

print(capture([
              [0,1,0],
              [1,9,1],
              [0,1,9],
                    ]))
