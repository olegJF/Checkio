# -*- coding: utf-8 -*-

def broken_clock(s_time, w_time, error_description):
    from datetime import time
    s_time = (int(s_time[:2])*60*60) + (int(s_time[3:5])*60) +int(s_time[6:])
    w_time = (int(w_time[:2])*60*60) + (int(w_time[3:5])*60) +int(w_time[6:])
    dif_time = w_time - s_time
    error_description = error_description.split(' at ')
    
    for i in range(len(error_description)):
        a,b = error_description[i].split(' ')
        if 'sec' in b:
            error_description[i] = int(a)
        elif 'min' in b:
            error_description[i] = int(a)*60
        elif 'hour' in b:
            error_description[i] = int(a)*60*60
    correction = error_description[0]+ error_description[1]
    true_time = int(s_time+(dif_time/correction)*error_description[1])
    #print('s_time=',s_time,' w_time',w_time, ' correction=',correction)
    hh = true_time//3600
    mm = (true_time%3600)//60
    ss = (true_time%3600)%60
    true_time = time(hh,mm,ss)

    return true_time.isoformat()
    

print(broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours'))

"""    
def broken_clock(starting_time, wrong_time, error_description):
    s = datetime.datetime.strptime(starting_time, '%H:%M:%S')
    w = datetime.datetime.strptime(wrong_time, '%H:%M:%S')
    d = w - s
    t1, u1, _, t2, u2 = error_description.split()
    m = {'h': 3600, 'm': 60, 's': 1}
    dt = int(t1) * m[u1[0]]
    p = int(t2) * m[u2[0]]
    t = s + datetime.timedelta(0, int(d.seconds * p / (p + dt)))

    return str(t.time())
"""
