# -*- coding: utf-8 -*-

##def probability(dice_number, sides, target):
##    import itertools
##    if dice_number*sides < target: return round(0.0, 4)
##    c = [i for i in range(1,(sides+1))]
##    count = 0
##    d = [i for i in itertools.product(c, repeat=dice_number) if sum(i) == target]
##    
##        
##    return round(len(d)/sides**dice_number,4)

def probability(dice_number, sides, target):

    if dice_number*sides < target or target < dice_number: return 0.0000
    prob = {i:1/sides for i in range(1, sides+1)}
    CONST = 1/sides
    for i in range(1, dice_number):
        #print('i',i , 'prob', prob)
        tmp = []
        for x in range(len(prob)+1):
            if x != 0:
                tmp.append(prob[x]*CONST)
            else: tmp.append(0)
        #print('len tmp',len(tmp),'tmp', tmp)
        for k,v in prob.items(): prob[k] = 0
        for y in range(i,len(tmp)):
            for z in range(1, sides+1):
                if prob.get(y+z) != None:
                    prob[y+z] = prob[y+z] + tmp[y]
                else: prob[y+z] = tmp[y]
            
    return round(prob[target], 4)

print(probability(10, 10, 50))



