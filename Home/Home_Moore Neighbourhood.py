# -*- coding: utf-8 -*-

data=(
((1,0,1,0,1),
(0,1,0,1,0),
(1,0,1,0,1),
(0,1,0,1,0),
(1,0,1,0,1),
(0,1,0,1,0),), 5, 4)

grid, row, col=data
#print(len(grid[0]))

def find_neighbours(grid, row, col):
    if row==0:
        x_min=0
    else:
        x_min=row-1
    if col==0:
        y_min=0
    else:
        y_min=col-1
        
    size_x_grid=len(grid)
    size_y_grid=len(grid[0])
    
    if row==size_x_grid-1:
        x_max=size_x_grid
    elif row>size_x_grid-1:
        return 0
    else:
        x_max=row+2
        
    if col==size_y_grid-1:
        y_max=size_y_grid
    elif col>size_y_grid-1:
        return 0
    else:
        y_max=col+2
    cnt=0
    for x in range(x_min,x_max):
        for y in range(y_min,y_max):
            if grid[x][y]==1:
                cnt+=1
    if grid[row][col]==1:
        cnt-=1
    return cnt


    

print(find_neighbours(grid, row, col))
