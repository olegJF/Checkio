# -*- coding: utf-8 -*-

def checkio(a,b,c):
    degree = []
    temp = sorted([a,b,c])
    if temp[2]>=temp[0]+temp[1]:
        return [0,0,0]
    import math
    alfa = math.degrees(math.acos(((b*b+c*c)-a*a)/(2*b*c)))
    if math.modf(alfa)[0]<0.5:
        alfa = math.modf(alfa)[1]
    else:
        alfa = math.ceil(alfa)
    beta = math.degrees(math.acos(((a*a+c*c)-b*b)/(2*a*c)))
    if math.modf(beta)[0]<0.5:
        beta = math.modf(beta)[1]
    else:
        beta = math.ceil(beta)
    gama = 180-(alfa+beta)
    degree = [int(alfa),int(beta),int(gama)]
    return sorted(degree)
    

print(checkio(10,20,30))
