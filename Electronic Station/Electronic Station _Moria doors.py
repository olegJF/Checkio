# -*- coding: utf-8 -*-
def total(word1, word2):
    if word1 == word2:
        return 100
    cnt = 0
    if word1[0]== word2[0]:
        cnt +=10
    if word1[-1]== word2[-1]:
        cnt +=10
    if len(word1)<=len(word2):
        cnt += (len(word1)/len(word2))*30
    else:
        cnt += (len(word2)/len(word1))*30
    cnt += (len(set(word1)&set(word2))/len(set(word1).union(set(word2))))*50
    return cnt

def checkio(message):
    a = message.lower().replace(',', ' ') .replace('.', ' ')
    words = a.split(' ')
    array = [[0 for i in range(len(words))] for e in range(len(words))]
    #print(words)
    #print(len(array))
    for x in range(0, len(words)):
        for y in range(0, len(words)):
            
            if x==y or words[x]=='' or words[y]=='':
                continue
            else:
                #print('x=',x,'; y=',y)
                array[x][y] = total(words[x], words[y])
                #print(array)
    matrix = []
    for i in range(len(array)):
        matrix.append(sum(array[i]))
    max_rez = matrix[0]
    max_index = 0
    for i in range(len(matrix)):
        if matrix[i]>=max_rez:
            max_rez = matrix[i]
            max_index = i
        
    return words[max_index]
    
    



print(checkio("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University."))
