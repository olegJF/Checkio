def a(arr):
    size = len(arr) - len(arr)%2
    for i in range(0, size, 2):
        arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr

print(a([1,2,3,4,5]))
