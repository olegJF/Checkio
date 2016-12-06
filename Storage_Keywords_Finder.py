# -*- coding: utf-8 -*-

def checkio(text, words):
    
    def words_not_in_text(text, words):
        res = True
        text = text.lower()
        for word in words:
            if word in text:
                res = False
                break
        return res

    if text == '' or words == '': return text
    words = words.lower().split(' ')
    if words_not_in_text(text, words): return text
    words_from_text = dict()
    list_from_text = text.split(' ')
    for word in list_from_text: words_from_text[word] = []
    #print(words_from_text)
    for word in words:
        if word in text.lower():
            for key in words_from_text:
                if word in key.lower():
                    words_from_text[key].append(word)
                else: pass
    for word in words_from_text:
        if '' in words_from_text[word]:
            words_from_text[word].remove('')
    #print(words_from_text)
    for word in words_from_text:
        #print(word, len(words_from_text[word]))
        if len(words_from_text[word]) > 0 and words_from_text[word] !='':
            borders = []
            for tag in words_from_text[word]:
                repeat = word.lower().count(tag)
                if repeat == 1:
                    begin = word.lower().index(tag)
                    end = len(tag)
                    borders.append([begin, begin+end])
                else:
                    if len(tag)*repeat == len(word):
                        borders.append([0, len(word)])
                    else:
                        size_of_tag = len(tag)
                        i = 0
                        while i<=(len(word)-(size_of_tag-1)):
                            print('i=', i, 'word',word, 'tag', tag)
                            if word[i:i+size_of_tag] == tag:
                                borders.append([i, i+size_of_tag])
                                i +=size_of_tag
                            else: i +=1
                borders = sorted(borders)
            if len(borders) > 1:
                for i in range(len(borders)-1):
                    for y in range(i, len(borders)-1):
                        if borders[i][1] > borders[y+1][0]:
                            # Merge overlapping areas
                            if borders[y+1][1] > borders[i][1]:
                                borders[i][1] = borders[y+1][1]
                            borders[y+1][0] = 0
                            borders[y+1][1] = 0
                    begin, end = borders[i]
                    begin1, end1 = borders[i+1]
                    if word[begin: end] == word[begin1: end1]:
                        borders[i][1] = borders[i+1][1]
                        borders[i+1][0] = 0
                        borders[i+1][1] = 0
                        
                tmp = []
                for pair in borders:
                    if pair != [0,0]:
                        tmp.append(pair)
                borders = tmp
            borders = sorted(borders)
            new_word = ''
            for i in range(len(borders)):
                if i ==0 and borders[i][0] > 0:
                    new_word +=word[0: borders[i][0]]
                elif i!=0 and borders[i-1][1] < borders[i][0]:
                    new_word +=word[borders[i-1][1]: borders[i][0]]
                new_word +='<span>'+word[borders[i][0]: borders[i][1]]+'</span>'
                if i == len(borders)-1 and borders[i][1]<len(word):
                    new_word +=word[borders[i][1]:]
            words_from_text[word] = new_word
            
        else:
            words_from_text[word] = word
    #print(words_from_text)
    word = ''
    new_text = ''
    for i in range(len(text)):
        if text[i] != ' ' or i == len(text)-1:
            word += text[i]
        if text[i] == ' ' or i == len(text)-1:
            space = ''
            if text[i] == ' ': space = ' '
            new_text += words_from_text[word] + space
            word = ''
    return new_text

#print(checkio("123456789", "3 6"))
