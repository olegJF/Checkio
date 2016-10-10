# -*- coding: utf-8 -*-

def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1
    
        



    
     
    

print(checkio("AF", 16))
