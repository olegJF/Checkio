# -*- coding: utf-8 -*-
data=("Lorem ipsum dolor sit amet")
def checkio(data):
    import collections
    import string
    temp={}
    e=[]
    ascii_string = string.ascii_lowercase
    for letter in data.lower():
        if letter in ascii_string:
            if letter in temp:
                temp[letter] += 1
            else:
                temp[letter] = 1
            
    e = temp.keys()
    e = sorted(e)
    max_digit = int(max(temp.values()))
    for i in e:
        if int(temp[i])==max_digit:
            return i

print(checkio(data))


