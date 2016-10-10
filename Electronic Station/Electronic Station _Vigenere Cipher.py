# -*- coding: utf-8 -*-
def getSecretWord(array):
    word = []
    if array.count(array[0])==len(array):
        word.append(array[0])
        return word
    for i in range(len(array)):
        if array[i] not in word: word.append(array[i])
        else:
            if i<len(array) and i+1<len(array):
                if array[i]==word[0] and array[i+1]==word[1]:
                    break
                else: word.append(array[i])
    return word
            
def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    shifr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    secret_word = []
    decoded_word = ''
    for i in range(len(old_encrypted)):
        tmp = shifr.find(old_encrypted[i])-shifr.find(old_decrypted[i])
        if tmp<0: tmp +=26
        secret_word.append(tmp)
    print(secret_word)
    print(getSecretWord(secret_word))
    if len(new_encrypted)>len(secret_word):
        word = getSecretWord(secret_word)
        full = int(len(new_encrypted)/len(word))
        tail = int(len(new_encrypted)%len(word))
        #print('full',full,'tail',tail)
        secret_word = []
        for i in range(full):
            for y in word: secret_word.append(y)
        #print('new',secret_word)
        for i in range(tail): secret_word.append(word[i])
    #print(len(new_encrypted),'sw',len(secret_word))
    for i in range(len(new_encrypted)):
        tmp = shifr.find(new_encrypted[i])- secret_word[i]
        decoded_word +=shifr[tmp]
    return decoded_word
"""
print(decode_vigenere("ALLRIGHTALLRIGHTBUTAPARTFROMBETTERSANITATIONANDMEDICINEANDEDUCATIONANDIRRIGATIONANDPUBLICHEALTHANDROADSANDAFRESHWATERSYSTEMANDBATHSANDPUBLICORDERWHATHAVETHEROMANSEVERDONEFORUS",
                      "OZZFWUVHOZZFWUVHPIHODOFHTFCAPSHHSFGOBWHOHWCBOBRASRWQWBSOBRSRIQOHWCBOBRWFFWUOHWCBOBRDIPZWQVSOZHVOBRFCORGOBROTFSGVKOHSFGMGHSAOBRPOHVGOBRDIPZWQCFRSFKVOHVOJSHVSFCAOBGSJSFRCBSTCFIG",
                      "WHGBCHDWBWBUWHGDOGGSRCBHVWGDOFFCHWGBCACFSWHVOGQSOGSRHCPSWHGSLDWFSROBRUCBSHCASSHWHGAOYSFHVWGWGOZOHSDOFFCHWHGOGHWTTPSFSTHCTZWTSWHFSGHGWBDSOQSWTMCIVORBHBOWZSRWHHCHVSDSFQVWHKCIZRPSDIGVWBUIDHVSROWGWSGWHGFIBURCKBHVSQIFHOWBOBRXCWBSRHVSQVCWFWBJWGWPZSHVWGWGOBSLDOFFCH"))
"""
def get_key(decrypted,encrypted):
    key,lastind=[],1
    for i,(plain,cypher) in enumerate(zip(decrypted,encrypted)):
        print('i=', i, 'plain=',plain,'cypher=',cypher)
        key_char=chr((ord(cypher)-ord(plain))%26+65)
        print('key_char',key_char)
        key.append(key_char)
        print('key_char!=key[i%lastind]=',key_char!=key[i%lastind])
        print('i%lastind',i%lastind)
        # поиск последнего элемента секретного слова
        # lastind увеличивается до тех пор, пока не пойдут повторы букв
        if key_char!=key[i%lastind]:
            lastind=i+1
            print('lastind=',lastind)

    return key[:lastind]

print(get_key('DONTWORRYBEHAPPY','FVRVGWFTFFGRIDRF'))
