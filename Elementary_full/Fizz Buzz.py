# -*- coding: utf-8 -*-

def checkio(number):
    result = ''
    if number%3==0:
        result +='Fizz'
        if number%5==0:
            result +=' Buzz'
            return result
    elif number%5==0:
        result +='Buzz'
    else:
        result +=str(number)
    return result    
    
    

print(checkio(50))
