# -*- coding: utf-8 -*-
def findD(m):
    a = (m[0][0]*m[1][1]*m[2][2])+(m[2][0]*m[0][1]*m[1][2])+(m[1][0]*m[2][1]*m[0][2])
    b = (m[2][0]*m[1][1]*m[0][2])
    c = (m[0][0]*m[2][1]*m[1][2])
    d = (m[1][0]*m[0][1]*m[2][2])
    return a-b-c-d

def checkio(string):
    from math import sqrt
    string = string.replace('(','') .replace(')','').replace(' ','')
    b = string.split(',')
    main = [[0 for i in range(3)] for y in range(3)]
    d1 = [[0 for i in range(3)] for y in range(3)]
    d2 = [[0 for i in range(3)] for y in range(3)]
    d3 = [[0 for i in range(3)] for y in range(3)]
    S = [] 
    for i in range(3):
        main[i][0] = int(b[i*2])
        main[i][1] = int(b[i*2+1])
        main[i][2] = 1
        S.append((-1)*((int(b[i*2])**2)+(int(b[i*2+1])**2)))
    D = findD(main)
    
    for i in range(3):
        d1[i][0] = S[i]
        d1[i][1] = main[i][1]
        d1[i][2] = main[i][2]
        
        d2[i][0] = main[i][0]
        d2[i][1] = S[i]
        d2[i][2] = main[i][2]
        
        d3[i][0] = main[i][0]
        d3[i][1] = main[i][1]
        d3[i][2] = S[i]
    D1 = findD(d1)
    D2 = findD(d2)
    D3 = findD(d3)
    A = D1/D
    B = D2/D
    C = D3/D
    x0 = str(-1*A/2) .split('.')
    y0 = str(-1*B/2) .split('.')
    R = str((sqrt(A**2+B**2-4*C))/2) .split('.')
    for i in (x0,y0,R):
        if i[1]!='0' and i[1][:2]!='00':
            i[0] = str(round(float(i[0]+'.'+i[1]),2))
            
    return '(x-'+x0[0]+')^2+(y-'+y0[0]+')^2='+R[0]+'^2'
    
    



print(checkio(33))
