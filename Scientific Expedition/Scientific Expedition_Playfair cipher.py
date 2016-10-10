# -*- coding: utf-8 -*-
def getSecretTable(text):
    text = text.lower()
    raw_string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    new_string = ''
    for i in text:
        if i.isalnum() and i not in new_string: new_string +=i
    for i in raw_string:
        if i not in new_string: new_string +=i
    x = 0
    table = [[x for i in range(6)] for y in range(6)]
    for i in range(6):
        for y in range(6):
            table[i][y] = new_string[x]
            x +=1
    return table    

def getCouple(text):
    couples = []
    for i in range(0,len(text),2): couples.append(text[i:i+2])
    return couples

def getString(matrix):
    new_string = ''
    for couple in matrix: new_string +=couple
    return new_string

def isDouble(matrix):
    for couple in matrix:
        if len(couple)==2 and couple[0]==couple[1]:
            return couple[0], matrix.index(couple)
    return False

def changeCouple(text, letter, position):
    num = position*2
    if letter=='x': add='z'
    else: add='x'
    if num==len(text)-2:
        text = text[:num]+letter+add+letter+add
    else:
        text = text[:num]+letter+add+letter+text[num+2:]
    return text

def getNumbers(table, couple):
    first, second = 0,0
    cycle = 0
    for row in table:
        if couple[0] in row: first = cycle
        if couple[1] in row: second = cycle
        cycle +=1
    return first, second

def getRow(table, couple):
    first, second = 0,0
    cycle = 0
    for i in range(len(table)):
        column = [row[i] for row in table]
        if couple[0] in column: first = cycle
        if couple[1] in column: second = cycle
        cycle +=1
    return first, second

def getThreeLetters(text):
    for i in text:
        if i=='x': add='z'
        else: add='x'
        if i+add+i in text:
            return i+add+i
    return False
        

def encode(message, key):
    table = getSecretTable(key)
    massage = message.lower()
    new_string = ''
    for i in massage:
        if i.isalnum(): new_string +=i

    matrix_for_encode = getCouple(new_string)
    #print(matrix_for_encode)
    while isDouble(matrix_for_encode):
        
        letter, num = isDouble(matrix_for_encode)
        #print(letter, num)
        new_string = getString(matrix_for_encode)
        new_string = changeCouple(new_string, letter, num)
        matrix_for_encode = getCouple(new_string)
        #print('----------------------------')
        #print(matrix_for_encode)
        #input('&?')
    size = len(matrix_for_encode)-1
    last_couple = matrix_for_encode[size]
    if len(last_couple)==1:
        if last_couple =='z':
            matrix_for_encode[size]=last_couple+'x'
        else: matrix_for_encode[size]=last_couple+'z'

    print(getString(matrix_for_encode))
        
    encoding_matrix = []
    size = len(table[0])-1
    for couple in matrix_for_encode:
        first, second = getNumbers(table, couple)
        col1, col2 = getRow(table, couple)
        letter_first, letter_second = '',''
        if first == second:
            if table[first].index(couple[0])==size:
                letter_first = table[first][0]
                letter_second = table[first][table[first].index(couple[1])+1]
            elif table[first].index(couple[1])==size:
                letter_second = table[first][0]
                letter_first = table[first][table[first].index(couple[0])+1]
            else:
                letter_first = table[first][table[first].index(couple[0])+1]
                letter_second = table[first][table[first].index(couple[1])+1]
            encoding_matrix.append(letter_first+letter_second)
        elif col1 == col2:
            if first==size:
                letter_first = table[0][col1]
                letter_second = table[second+1][col2]
            elif second ==size:
                letter_first = table[first+1][col1]
                letter_second = table[0][col2]
            else:
                letter_first = table[first+1][col1]
                letter_second = table[second+1][col2]
            encoding_matrix.append(letter_first+letter_second)
        else:
            letter_first = table[first][col2]
            letter_second = table[second][col1]
            encoding_matrix.append(letter_first+letter_second)
    return  getString(encoding_matrix)


def decode(secret_message, key):
    table = getSecretTable(key)
    matrix_for_encode = getCouple(secret_message)
    size = len(table[0])-1
    encoding_matrix = []
    for couple in matrix_for_encode:
        first, second = getNumbers(table, couple)
        col1, col2 = getRow(table, couple)
        if first == second:
            if table[first].index(couple[0])==0:
                letter_first = table[first][size]
                letter_second = table[first][table[first].index(couple[1])-1]
            elif table[first].index(couple[1])==0:
                letter_second = table[first][size]
                letter_first = table[first][table[first].index(couple[0])-1]
            else:
                letter_first = table[first][table[first].index(couple[0])-1]
                letter_second = table[first][table[first].index(couple[1])-1]
            encoding_matrix.append(letter_first+letter_second)
        elif col1 == col2:
            if first==0:
                letter_first = table[size][col1]
                letter_second = table[second-1][col2]
            elif second ==0:
                letter_first = table[first-1][col1]
                letter_second = table[size][col2]
            else:
                letter_first = table[first-1][col1]
                letter_second = table[second-1][col2]
            encoding_matrix.append(letter_first+letter_second)
        else:
            letter_first = table[first][col2]
            letter_second = table[second][col1]
            encoding_matrix.append(letter_first+letter_second)
    """
    size = len(encoding_matrix)-1
    if encoding_matrix[size] == encoding_matrix[size-1]:
        encoding_matrix[size] = encoding_matrix[size][0]
        encoding_matrix[size-1] = encoding_matrix[size-1][0]
    """
    encoding_string = getString(encoding_matrix)
    """
    while getThreeLetters(encoding_string):
        code = getThreeLetters(encoding_string)
        num = encoding_string.find(code)
        encoding_string = encoding_string[:num+1]+encoding_string[num+2:]
    """
    return encoding_string

encode("Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country", "42")
#print(encode("Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country", "42"))
print(decode("g2xl2s4yg64hijpbznk3luapu0tzcgmtg2xlulnsifiutousjftqpl2mgcbm4dpoummbtzgcznfqfkjuhqif2nhobvfwutqgmds2qhbvifxmjufjthl0plsgqlymulqjufhisbrzzni4mctulizngqgkbmuhau2m2shfm2mhschfuig4mbys2mrxjufqmbkg21cv4jlhmpyqazznfjvlm24ibmavvokmjfugqzhunzifkh4iryygsxqfhfof2mgchugudm2sb4gugkbsoiiutousz0", "42"))
#"g2xl2s4yg64hijpbznk3luapu0tzcgmtg2xlulnsifiutousjftqpl2mgcbm4dpoummbtzgcznfqfkjuhqif2nhobvfwutqgmds2qhbvifxmjufjthl0plsgqlymulqjufhisbrzzni4mctulizngqgkbmuhau2m2shfm2mhschfuig4mbys2mrxjufqmbkg21cv4jlhmpyqazznfjvlm24ibmavvokmjfugqzhunzifkh4iryygsxqfhfof2mgchugudm2sb4gugkbsoiiutousz0", "42"
