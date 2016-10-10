# -*- coding: utf-8 -*-
def check_connection(data, first, second):
    all_connection = []
    for pair in data:
        x,y = pair.split('-')
        all_connection.append([x,y])
    temp = []
    temp.append(first)
    for i in temp:
        #print('i=',i)
        for pair in all_connection:
            if i in pair and pair[1-pair.index(i)] not in temp:
                temp.append(pair[1-pair.index(i)])
                print(temp)
                if second in temp:
                    return True


    return False

data = check_connection(

    ("a-b", "b-c", "c-a", "d-e",

     "e-f", "f-g", "g-h", "g-j","f-i","e-j"),

    "j", "i")
print(data)
