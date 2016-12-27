# -*- coding: utf-8 -*-


def che(required, tasks):
    painted = [tasks[i][1] - (tasks[i][0] - 1) for i in range(len(tasks))]
    i = 1
    while i < len(tasks):
        # print(tasks, 'i=', i)
        for x in range(i):
            if tasks[i][0] >= tasks[x][0] and tasks[i][1] <= tasks[x][1]:
                tasks[i][0] = 0
                tasks[i][1] = 0
                painted[i] = 0
                # print('1', 'tasks[i]', tasks[i])
            elif tasks[x][0] >= tasks[i][0] and tasks[x][1] <= tasks[i][1]:
                tasks[x][0] = 0
                tasks[x][1] = 0
                painted[i] -= painted[x]
                # print('2', 'tasks[i]', tasks[i])
            elif tasks[i][0] <= tasks[x][0] and tasks[i][1] >= tasks[x][0]:
                dif = tasks[i][1] - tasks[x][0] + 1
                tasks[i][1] = tasks[x][1]
                tasks[x][0] = 0
                tasks[x][1] = 0
                painted[i] -= dif
                # print('3', 'tasks[i]', tasks[i], 'dif', dif)
            elif tasks[i][0] >= tasks[x][0] and tasks[i][0] <= tasks[x][1] and tasks[i][1] >= tasks[x][1]:
                dif = tasks[x][1] - tasks[i][0] + 1
                tasks[i][0] = tasks[x][0]
                tasks[x][0] = 0
                tasks[x][1] = 0
                painted[i] -= dif
                # print('4', 'tasks[i]', tasks[i], 'dif', dif)
        i += 1
    # print(tasks)
    if required > sum(painted): return -1
    tmp, i = 0, 0
    while tmp < required:
        tmp += painted[i]
        i += 1

    return i


print(che(612742616513000, [[858310018365524, 902063077244091], [932665378449117, 1028409672338264],
                            [882165278163239, 957945652291761], [155331862264691, 231608087199557],
                            [309323812898016, 328794059405147], [311727991597994, 391226174154816],
                            [826415306967097, 893972043882819], [170753995991478, 221100797836809],
                            [472995836315594, 478902758061898], [779003863306990, 822734502976504],
                            [539843675072188, 554844466580541], [977564633426502, 991018537238369],
                            [889461015856698, 901719104033374], [268288887276466, 292053591549963],
                            [87698520389374, 109261297832598], [650723837467456, 729926149124749],
                            [627448683684809, 644021001384284], [264317870081369, 322309330307873],
                            [238729907671924, 290743490959244], [938382837602825, 955450166170994]]))
