hill = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6, 8]
]
res = {}
for i in range(len(hill) - 1, 0, -1):
    tmp = []
    for y in range(len(hill[i]) - 1, 0, -1):
        x = hill[i][y] + hill[i-1][y-1]
        z = hill[i][y-1] + hill[i-1][y-1]
        tmp.append(max(x,z))
        hill[i-1][y-1] = max(x,z)
    tmp = list(reversed(tmp))
    res[i] = tmp
print(res)
print(hill)
