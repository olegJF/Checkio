# -*- coding: utf-8 -*-

def a(b):
    b +=1
    def c():
        global b
        b +=2
        print(b)
        return(b)
    b = c()
    return b
print(a(1))



