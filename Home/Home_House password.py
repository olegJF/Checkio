# -*- coding: utf-8 -*-

data='rrrrri$$o2'
def tre(data):
    import re
    if len(data)<=9:
        return False
    elif re.search('[A-Z]',data)==None:
        return False
    elif re.search('[a-z]',data)==None:
        return False
    elif re.search('[0-9]',data)==None:
        return False
    return True

print(tre(data))
