def nearest_square(number):
    low = number - 1
    high = number + 1
    res = None
    while True:
        if float.is_integer(high**0.5):
            res = high
            break
        high += 1
        if low > 0:
            if float.is_integer(low**0.5):
                res = low
                break
            low -= 1
        
    return res

if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")
