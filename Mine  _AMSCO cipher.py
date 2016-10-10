# -*- coding: utf-8 -*-
from math import floor, ceil
def code(string, key):
    size_x = len(str(key))
    size_y = ceil(len(string)/floor(1.5*size_x))
    matrix = [['' for i in range(size_x)] for y in range(size_y)]
    for y in range(size_y):
        for x in range(size_x):
            if string:
                if y==0 or y%2==0:
                    if x==0 or x%2==0:
                        matrix[y][(int(str(key)[x]))-1] = string[0]
                        if len(string) >1:string = string[1:]
                        else: string = ''
                    else:
                        if len(string)>2:
                            matrix[y][(int(str(key)[x]))-1] = string[0:2]
                            string = string[2:]
                        else:
                            matrix[y][(int(str(key)[x]))-1] = string[:]
                            string = ''
                else:
                    if x==0 or x%2==0:
                        if len(string)>2:
                            matrix[y][(int(str(key)[x]))-1] = string[0:2]
                            string = string[2:]
                        else:
                            matrix[y][(int(str(key)[x]))-1] = string[:]
                            string = ''
                        
                    else:
                        matrix[y][(int(str(key)[x]))-1] = string[0]
                        if len(string) >1:string = string[1:]
                        else: string = ''
            #print(matrix[int(str(key)[x])][y])
    return matrix

def decode_amsco(string, key):
    size_x = len(str(key))
    column_hight = 0
    
    if size_x%2==0:
        size_y = ceil(len(string)/floor(1.5*size_x))
        size_line = floor(1.5*size_x)
    else:
        size_line_odd = floor(1.5*size_x)
        size_line_even = ceil(1.5*size_x)
        double_row_size = size_line_odd + size_line_even
        size_y = ceil(len(string)/(double_row_size/2))
        size_line = double_row_size/2
    for i in range(size_y): column_hight +=2-(i%2)
    #print('column_hight=',column_hight, 'size_y=',size_y)
    cnt_for_odd_arr = [column_hight-(1-((str(key).find(str(1))%2)))*(size_y%2)]
    for i in range(1,len(str(key))):
        position = str(key).find(str(i+1))
        #print('position',position)
        cnt_for_odd_arr.append(cnt_for_odd_arr[i-1]+(column_hight-(1-round(position%2))*(size_y%2)))
    print(cnt_for_odd_arr)
    #print('column_hight=',column_hight, 'size_x',size_x, 'size_y=',size_y)
    #print('size_line=',size_line,'len(string=',len(string),'len(string)%size_line=',len(string)%size_line)
    if size_y%2==0: added = [2,3]
    else: added = [1,3]
    #for i in range(size_x-2): added.append(added[i]+3)
    #print(added)
    matrix = [[1+ abs((i%2)-(y%2)) for i in range(size_x)] for y in range(size_y)]
    #print(len(matrix))
    if len(string)%size_line != 0:
        #full_line = int((len(string)//size_line)*size_line)
        miss_letters = cnt_for_odd_arr[-1]-len(string)
        empty_column = ceil(miss_letters/1.5)
        fill_column = len(str(key))- empty_column-1
        print('miss_letters',miss_letters, 'empty_column',empty_column, 'fill_column=',fill_column)
        #if size_x%2!=0: size_line = int(size_line)+ floor(size_y%2)
        tmp = 0
        for y in range(fill_column+1,size_x): tmp +=matrix[size_y-1][y]
        overflow = False
        if len(string)+tmp>cnt_for_odd_arr[-1]: overflow = True
        
        
        for i in range(1,size_x+1): # надо сделать, чтобы отсчет шел с 1 группы, вопрос как подсчитать необх. длину столбца
            first, last = '', ''
            x = (str(key)).find(str(i)) #position of number
            #print('len(string)=', len(string))
            #print('x=', x, 'i=', i,'full_line + added[x]', full_line + added[x], 'len(string)=', len(string))
            if x>fill_column:
                #print('x=', x, 'i=', i, 'size_y-1', size_y-1)
                diff =matrix[size_y-1][x]
                if overflow and x==fill_column+1: diff -=1
                empty = '.'* diff
                length = cnt_for_odd_arr[i-1]
                #print('(x)*column_hight+(column_hight-diff)',(x)*column_hight-diff)
                print( 'x=', x, 'i=', i,'diff',diff,'length',length)
                first = string[:length-diff]
                #print('first',first)
                last =  string[length-diff:]
                #print('last',last)
                string =first+empty+last
                #print(string)
    print(string)            
    d_tmp = []
    matrix = [[1+ abs((i%2)-(y%2)) for i in range(size_x)] for y in range(size_y)]
    #print('size_line',size_line,'len(string',len(string))
    if size_line>=len(string):
        for i in range(size_x):
            column = (str(key)).find(str(i+1))
            odd_x = floor(column%2)
            matrix[0][column] = string[:1+odd_x]
            string=string[1+odd_x:]
    else:
        for i in range(size_x):
            column = int(str(key)[i])-1
            #print('column =',column)
            if column ==0:
                d_tmp.append(string[0:cnt_for_odd_arr[column]])
            elif column == size_x-1:
                d_tmp.append(string[cnt_for_odd_arr[column-1]:])
            else:
                begin,end = cnt_for_odd_arr[column-1],cnt_for_odd_arr[column]
                d_tmp.append(string[begin:end])
        print(d_tmp)
    
        for x in range(size_x):
            #odd_x = floor(x%2)
            for y in range(size_y):
                cnt_ltr = matrix[y][x]
                matrix[y][x] = d_tmp[x][0:cnt_ltr] .replace('.','')
                d_tmp[x] = d_tmp[x][cnt_ltr:]
                #odd_y = floor(y%2)
                #if not odd_x:# если четные
                   # matrix[y][x] = d_tmp[x][0:1+odd_y] .replace('.','')
                    #d_tmp[x] = d_tmp[x][1+odd_y:]
                #else:
                    #matrix[y][x] = d_tmp[x][0:2-odd_y] .replace('.','')
                    #d_tmp[x] = d_tmp[x][2-odd_y:]
    #print(matrix)
    dec_string = ''

                
    for i in range(len(matrix)): dec_string += ''.join(matrix[i])
    return dec_string 
                
            

print( decode_amsco("oruoreemdstmioitlpslam", 4123))
#(int(str(key)[x]))-1
#"oruoreemdstmioitlpslam", 4123  oruoreemdst.mioit.lpslam 
#"hrewhoorrowyilmmmoaouletow", 123
#'kicheco', 23415
#"lsesanaeamiauelodosadonpieulneittgemtdsorstenomemalorccicegnsutadalirpmeritolomcoiengae", 654287931
#"cmpduiuzyowerovkbsogqxjaheoaltnfr", 87621543
#'fuynpnireeesgwowhiancxitwhethsemheaodiiseaisttmieiogarepmettasaanhovythodtaikeeonfoydbrsstsawoeassfmoheofscwiemaeareishtelulepprbshitmqunneahoadrnkesntenertiwleyeepndmsutsuhtrareaygaeitdenaksenlesiriehmaontofeposfoslimmynrbxseeletlenldbwietttndtertttehelswreaistufamblosaweannerriteiotikwngnnjyrteheeintcrrofksoddsequntrxhactsblensthmoyhawerhnwlleiarndirppcpeefmnstmtoryalshosoesttmohiyoladfhsthicaeboinarfantsofnteiytsncfsioreeifiagrnoieltvauhenesrftelitutatehncnretesyulsrnphithelelmncswadissiayieoeeeericegleupaaglaenaelveaswhtvamoumernhereiageefellinua',526341


# интересное решение!!!
def amsco(mode, message, key):
    """AMSCO cipher (mode = 1 to encode, -1 to decode)"""
    n = row = ool = char = 0
    grid, idx = {}, str(key)
    # Put message characters in grid
    while n < len(message):
        grid[idx[ool], row, char], n, char = n, n + 1, char + 1
        if char > (row + ool) % 2:
            char, ool = 0, ool + 1
            if ool == len(idx):
                ool, row = 0, row + 1
    # Compute translation table
    table = dict((n, grid[k])[::mode] for n, k in enumerate(sorted(grid)))
    # Assemble characters in right order
    return ''.join(message[table[n]] for n in range(len(message)))


from functools import partial
encode_amsco, decode_amsco = partial(amsco, 1), partial(amsco, -1)

