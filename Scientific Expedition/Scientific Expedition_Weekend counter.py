# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime
def checkio(data1,data2):
    result = 0
    delta = (data2-data1).days
    
    for i in range(delta+1):
        now = (data1+timedelta(days=i)).isoweekday()
        if now==6 or now==7:
            result += 1
    return result
    

print(checkio(date(2013,2,2), date(2013,2,3)))
