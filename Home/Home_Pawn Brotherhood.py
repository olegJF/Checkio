# -*- coding: utf-8 -*-
def new_bord():
    return [[0 for y in range(8)]for x in range(8)]

def get_coordinate(couple):
    letters='abcdefgh'
    row = 8-int(couple[1:])
    col = letters.find(couple[0:1])
    return row,col
letters='abcdefgh'
def safe_pawns(pawns):
    temp = new_bord()
    result = 0
    for coord in pawns:
        row,col = get_coordinate(coord)
        temp[row][col] = 1
    #print (temp)
    for x in range(8):
        if 1 in temp[x]:
            #print('1 in line',8-x)
            for i in range(8):
                if temp[x][i]==1 and x!=7:
                    #print('pole',letters[i:i+1],8-x)
                    flag = True
                    if i==0:
                       x_left=8
                    else:
                        x_left=i-1
                    #print(letters[x_left:x_left+1])
                    if i<7:
                        x_right = i+1
                    else:
                        x_right = 8
                    #print('x_left=',x_left,'temp[x+1][x_left]=',temp[x+1][x_left])
                    if x_left!=8 and temp[x+1][x_left]==1:
                        result +=1
                        #print('Add result')
                        flag = False
                    if x_right!=8 and flag:
                        result +=temp[x+1][x_right]
    return result


couple='a4'
a = safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"})
print(a)


