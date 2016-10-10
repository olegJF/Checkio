# -*- coding: utf-8 -*-
def isCoupleInList(temp, matrix):
    a,b = temp
    if [a,b]in matrix or [b,a] in matrix:
        return True
    return False

def checkio(lines_list):
    result = 0
    for i in range(12):
        if i==4 or i==8:
            continue
        else:
            if isCoupleInList([i,i+1],lines_list) and isCoupleInList([i,i+4], lines_list):
                if isCoupleInList([i+4,i+5],lines_list) and isCoupleInList([i+1,i+5],lines_list):
                    result +=1
                    
    print(result)                
    for i in [1,2,5,6]:
        if isCoupleInList([i,i+1],lines_list) and isCoupleInList([i+1,i+2],lines_list):
            if isCoupleInList([i,i+4],lines_list) and isCoupleInList([i+4,i+8],lines_list):
                if isCoupleInList([i+2,i+6],lines_list) and isCoupleInList([i+6,i+10],lines_list):
                    if isCoupleInList([i+8,i+9],lines_list) and isCoupleInList([i+9,i+10],lines_list):
                        result +=1
    temp = 0
    for i in range(1,4):
        if isCoupleInList([i,i+1],lines_list) and isCoupleInList([i+12,i+13],lines_list):
            temp += 2
        
    for i in [1,5,9]:
        if isCoupleInList([i,i+4],lines_list) and isCoupleInList([i+3,i+7],lines_list):
            temp += 2
    if temp==12:
        result +=1
        
    
    return result

        
        
        
 
    
        
    
    

print(checkio([[1,5],[2,3],[4,8],[5,9],[8,12],[9,13],[14,15],[13,14],[12,16],[15,16]]))
