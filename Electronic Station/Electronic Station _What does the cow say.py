# -*- coding: utf-8 -*-
COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def cowsay(text):
    text = text.replace('  ',' ') .replace('   ',' ') .replace('   ',' ') .replace('  ',' ')
    tmp = []
    begin_line = '\n '
    end_line = ' '
    if len(text)<40:
        width = len(text)+2
    else:
        while len(text)>39:
            if text[39]==' ':
                tmp.append(text[:39])
                text = text[40:]
            else:
                is_space = False
                for i in range(38,-1,-1):
                    if text[i]==' ':
                        is_space = True
                        #print('true! i=',i)
                        break
                if is_space:
                    if i==0: tmp.append(text[0])
                    else: tmp.append(text[:i])
                    text = text[i+1:]
                else:
                    tmp.append(text[:39])
                    text = text[39:]
        if len(text)>0:
             tmp.append(text)
        max_width = len(tmp[0])
        for string in tmp:
            if len(string)>max_width:
                max_width = len(string)
        width = max_width +2
    for i in range(width):
        begin_line +='_'
        end_line +='-'
    begin_line +='\n'
    #end_line +='\n'
    msg =''
    if len(tmp)==0:
        msg = '< '+text+' >\n'
    else:
        for i in range(len(tmp)):
            if len(tmp[i])<max_width:
                for y in range(max_width-len(tmp[i])):
                    tmp[i] +=' '
            if i==0:
                msg +='/ '+tmp[i]+' \\'+'\n'
            elif i==len(tmp)-1:
                msg +='\\ '+tmp[i]+' /'+'\n'
            else:
                msg +='| '+tmp[i]+' |'+'\n'
                
                
    return begin_line+msg+end_line+COW
    
    



print(cowsay(" 0123456789012345678901234567890123456789 "))
