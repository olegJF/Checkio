# -*- coding: utf-8 -*-

def getRow(row, column, size, array):
    tmp = []
    for i in range(size):
        tmp.append(array[row][i+column])
    return tmp

def isEqualNextRow(row, column, pattern, image):
    for i in range(1,len(pattern)):
        #print('pattern[i]', pattern[i])
        #print('image', getRow(row+i, column, len(pattern), image))
        if pattern[i]!=getRow(row+i, column, len(pattern[0]), image):
            return False
    return True
        
def checkio(pattern, image):
    size_img_x, size_img_y = len(image), len(image[0])
    size_p_x, size_p_y = len(pattern), len(pattern[0])
    row  = 0
    #print(size_p, size_img)
    while row<size_img_x-size_p_x+1:
        column = 0
        while column<size_img_y-size_p_y+1:
            #print('row=', row, 'column=', column, pattern[0]==getRow(row, column, size_p_y, image))
            if pattern[0]==getRow(row, column, size_p_y, image) and isEqualNextRow(row, column, pattern, image):
                #print(isEqual(row, column, pattern, image))
                for x in range(size_p_x):
                    for y in range(size_p_y):
                        image[row+x][column+y]+=2
                column +=size_p_y
                #print('column=', column)
                
            else:
                column +=1
        row +=1
            
    return image
    

print(checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
    
