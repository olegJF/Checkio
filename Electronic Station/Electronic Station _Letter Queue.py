# -*- coding: utf-8 -*-
def checkio(array):
    result = []
    for command in array:
        if command =='POP':
            if len(result)>0:
                del result[0]
        elif 'PUSH' in command:
            result.append(command[-1])
            
    
    return ''.join(result)



print(checkio(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]))
