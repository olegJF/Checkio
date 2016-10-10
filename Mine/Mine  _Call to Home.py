# -*- coding: utf-8 -*-

def total_cost(array):
    all_calls = []
    res = 0
    i = 0
    times = []
    for data in array:
        all_calls.append(data.split(' '))
        tmp = int(int(all_calls[i][2])/60)
        if int(all_calls[i][2])%60: tmp +=1
        all_calls[i][2] = tmp
        if i==0: times.append(tmp)
        else:
            if all_calls[i][0] == all_calls[i-1][0]:
                times[-1] = times[-1] +tmp
            else: times.append(tmp)
        i +=1
    for time in times:
        if time>100: res += 100+(time-100)*2
        else: res +=time
    return res
