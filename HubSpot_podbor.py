matrix = [[1, 3, 5], [3, 1, 5], [2, 5, 1]]

f,s,t = 91, -27, -5
temp = [0, 0, 0]
temp[0] += f
temp[1] += matrix[0][1] * f
temp[2] += matrix[0][2] * f

temp[0] += matrix[1][0] * s
temp[1] += s
temp[2] += matrix[1][2] * s

temp[0] += matrix[2][0] * t
temp[1] += matrix[2][1] * t
temp[2] += t
#print(temp)
temp = [n % 360 for n in temp]
print(temp)
