# -*- coding: utf-8 -*-
def checkio(food):
    hungry_birds = [0]
    not_empty = True
    birds = 2
    result = 0
    while not_empty:
        if food-len(hungry_birds)>0:
            hungry_birds = [i+1 for i in hungry_birds]
            food -= len(hungry_birds)
            if food-len(hungry_birds)>0:
                for i in range(birds): hungry_birds.append(0)
            
            birds +=1
            #print('food=',food,'hungry_birds =',hungry_birds)
        else:
            for i in range(len(hungry_birds)):
                #print('i=',i)
                if food >0:
                    hungry_birds[i] +=1
                    food -=1
                    #print('food=',food,'hungry_birds =',hungry_birds)
            not_empty = False
    
                
    
    for i in hungry_birds: 
        if i!=0: result +=1
    return result
    

print(checkio(5))
