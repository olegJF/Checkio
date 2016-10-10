# -*- coding: utf-8 -*-
def verify_anagrams(str_1,str_2):
    str_1 = str_1.lower().replace(' ','')
    str_2 = str_2.lower().replace(' ','')
    result = True
    for i in str_1:
        if str_1.count(i)!=str_2.count(i):
            result = False
    return result


print(verify_anagrams("Hello", "Ole Oh"))
