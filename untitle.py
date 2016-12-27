string = "kicheco"
key = 23415
matr = ['', '', '', '', '']
from math import floor
# print(string)
for i in range(5):
    column = (str(key)).find(str(i + 1))
    odd_x = floor(column % 2)
    # print('column=',column, 'i=',i, 'odd_x=',odd_x, 'string[:1+odd_x]=', string[:1+odd_x])
    matr[column] = string[:1 + odd_x]
    string = string[1 + odd_x:]
    # print(string)
# print(matr)
x = 4
arr = [[0 for i in range(x)] for y in range(x)]
for i in range(x):
    for y in range(x):
        # print('i=',i,'y=',y)
        arr[i][y] = 1 + abs(round(i % 2) - round(y % 2))
print(arr)
r = [[1 + abs(round(i % 2) - round(y % 2)) for i in range(3)] for y in range(7)]
print(r)
