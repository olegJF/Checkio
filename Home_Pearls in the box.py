# -*- coding: utf-8 -*-

def change( color_before,  line):
    color_after = {'w':'b', 'b':'w'}
    for i, marble in enumerate(line):
        if marble == color_before:
            line = line[:i]+color_after[marble]+line[i+1:]
            break
    return line

def checkio(marbles, step):
    all_steps = [[1,marbles]]
    cnt = len(marbles)
    now_step = 1
    z = 0
    while now_step < step:
        for i in range(2**(now_step-1)):
            prev_probability, line = all_steps[z]
            #print('line', line, 'z', z)
            if prev_probability == -1:
                all_steps.append([-1,''])
                all_steps.append([-1,''])
            else:
                if 'w' not in line:
                    line = change( 'b', line)
                    probability = prev_probability*1
                    all_steps.append([probability,line])
                    all_steps.append([-1,''])
                elif 'b' not in line:
                    line = change( 'w', line)
                    probability = prev_probability*1
                    all_steps.append([probability,line])
                    all_steps.append([-1,''])
                else:
                    for y in ('b','w'):
                        new_line = change( y, line)
                        probability = (line.count(y)/cnt)*prev_probability
                        all_steps.append([probability,new_line])
            z +=1
        now_step +=1
    #print(all_steps)
    begin = 2**(now_step-1)-1
    end = 2**now_step
    #print(len(all_steps))
    last_line = all_steps[begin:end]
    probability = 0
    for pair in last_line:
        if pair[0] != -1:
            probability += (pair[1].count('w')/cnt)*pair[0]
    return round(probability, 2)


print(checkio('bwbwbwb', 5))
