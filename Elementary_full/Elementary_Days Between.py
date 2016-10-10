# -*- coding: utf-8 -*-

def checkio(date1, date2):
    from datetime import date
    year1,month1,day1 = date1
    year2,month2,day2 = date2
    delta = (date(year1,month1,day1)-date(year2,month2,day2)).days
    return abs(delta)
    #return abs((datetime.date(*date1) - datetime.date(*date2)).days)                
        



    
     
    

print(checkio((2014, 1, 1), (2014, 8, 27)))
