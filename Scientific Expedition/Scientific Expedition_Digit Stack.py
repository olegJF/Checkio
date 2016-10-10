# -*- coding: utf-8 -*-
def digit_stack(commands):
    result = 0
    stack = []
    for command in commands:
        if 'PEEK' in command:
            if len(stack)==0:
                result +=0
            else:
                result +=stack[len(stack)-1]
        elif 'POP' in command:
            if len(stack)==0:
                result +=0
            else:
                result +=stack.pop()
        elif 'PUSH' in command:
            digit_str = command.replace(' ','').replace('PUSH','')
            if digit_str!='':
                stack.append(int(digit_str))
    
    return result
    

print(digit_stack(['PEEK',"PUSH 4", "PEEK","PUSH", "PEEK"]))
