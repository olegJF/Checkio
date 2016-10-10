# -*- coding: utf-8 -*-

def checkio(words_set):
    x=0
    for word_1 in words_set:
        
        for word_2 in words_set:
            x+=1
            if word_1!=word_2 and len(word_2)>len(word_1):
                print('word_1', word_1,'word_2', word_2, )
                try:
                    if word_2.index(word_1, len(word_2)-len(word_1)):
                        #S.endswith(str) Заканчивается ли строка S шаблоном str
                        return True
                except ValueError:
                    pass
    print(x)                
    return False
                    
        



    
     
    

print(checkio({"longest","aa","a"}))
