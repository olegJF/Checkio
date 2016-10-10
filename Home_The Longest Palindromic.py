# -*- coding: utf-8 -*-

def longest_palindromic(text):
    n = len(text)
    d1 = [0 for i in range(n)]
    d2 = [0 for i in range(n)]
    l = 0
    r = -1
    for i in range(n):
        if i > r: k = 1
        else: k = min(d1[l + r - i], r - i)

        while(0 <= i-k and i+k < n and text[i - k] == text[i + k]):
            k +=1
        d1[i] = k;
        if i + k - 1 > r :
            r = i + k - 1
            l = i - k + 1

    l=0
    r=-1
    for i in range(n):
        if i > r: k = 0
        else: k = min(d2[l + r - i + 1], r - i + 1)

        while(i + k < n and i - k - 1 >= 0 and text[i+k] == text[i - k - 1]):
            k +=1
        d2[i] = k;

        if i + k - 1 > r:
            l = i - k
            r = i + k - 1

    if max(d1) > max(d2):
        center = d1.index(max(d1))
        left = center-(max(d1)-1)
        right = center+(max(d1))
        #print('nechet')
        
    else:
        center = d2.index(max(d2))
        left = center-(max(d2))
        right = center+(max(d2))
        #print('chet')
    #print (center, left, right)

    return text[left:right]

print(longest_palindromic("aeaayeya"))
