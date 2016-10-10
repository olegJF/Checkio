# -*- coding: utf-8 -*-

def check_command(pattern, command):
    bin_dgt = ''
    for element in command:
        if element.isdigit(): bin_dgt +='0'
        else: bin_dgt +='1'
    #print(bin_dgt, int(bin_dgt, 2))
    if pattern == int(bin_dgt, 2): return True
    return False
   

print(check_command(127, "Checkio"))

