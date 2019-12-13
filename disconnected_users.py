def dfs(_graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start in _graph:
        for next in _graph[start] - visited:
            dfs(_graph, next, visited)
    return visited


def disconnected_users(net, users, source, crushes):
    new_net = []
    for pair in net:
        if pair[0] in crushes:
            continue
        elif pair[1] in crushes:
            pair[1] = ''
        new_net.append(pair)
    graph = {i[0]: set() for i in new_net}
    for pair in new_net:
        if pair[1]:
            graph[pair[0]].add(pair[1])
    available = dfs(graph, source)
    if available == set(crushes):
        available = []
    return sum(val for key, val in users.items() if key not in available)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"
    tests = [
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'C'],
                        ['C', 'D']
                    ], {
                        'A': 10,
                        'B': 20,
                        'C': 30,
                        'D': 40
                    },
                        'A', ['C']],
            "answer": 70,
            "explanation": [
                "Users from node C(30) and D(40) didn't get a message",
                ['',  '',   '',   '',   '',
                 'A', '',   'C',  '',   '',
                 '',  'B',  '',   'D',  '',
                 '',  '',   '',   '',   '',
                 '',  '',   '',   '',   '']
            ],
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'D'],
                        ['A', 'C'],
                        ['C', 'D']
                    ], {
                        'A': 10,
                        'B': 0,
                        'C': 0,
                        'D': 40
                    },
                        'A', ['B']],
            "answer": 0,
            "explanation": [
                "Only node B is crashed. A can get access to D through the node C. B doesn't have user, so crashing B doesn't close any user",
                ['',  '',  '',   '',   '',
                 '',  '',   'A',   '',   '',
                 '',  'B',  '',   'C',  '',
                 '',  '',   'D',   '',   '',
                 '',  '',  '',   '',   '']
            ],
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['A', 'C'],
                        ['A', 'D'],
                        ['A', 'E'],
                        ['A', 'F']
                    ], {
                        'A': 10,
                        'B': 10,
                        'C': 10,
                        'D': 10,
                        'E': 10,
                        'F': 10
                    },
                        'C', ['A']],
            "answer": 50,
            "explanation": [
                "Node A is in the center of network. It is the most crusual node. Crashing this node disconnectes all other nodes.",
                ['',  '',  '',   '',   '',
                 '',  '',  'B',  '',   '',
                 '',  'F', 'A',  'C',  '',
                 '',  '',  'E',  'D',  '',
                 '',  '',   '',  '',   '']
            ],
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'C'],
                        ['C', 'D']
                    ], {
                        'A': 10,
                        'B': 20,
                        'C': 30,
                        'D': 40
                    },
                        'A', ['B']],
            "answer": 90,
            "explanation": [
                "Users from node B(20), C(30) and D(40) didn't get a message",
                ['',  '',   '',   '',   '',
                 'A', '',   'C',  '',   '',
                 '',  'B',  '',   'D',  '',
                 '',  '',   '',   '',   '',
                 '',  '',   '',   '',   ''],
            ],
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'C'],
                        ['C', 'D']
                    ], {
                        'A': 10,
                        'B': 20,
                        'C': 30,
                        'D': 40
                    },
                        'A', ['D']],
            "answer": 40,
            "explanation": [
                "Only users from D(40) didn't get a message",
                ['',  '',   '',   '',   '',
                 'A', '',   'C',  '',   '',
                 '',  'B',  '',   'D',  '',
                 '',  '',   '',   '',   '',
                 '',  '',   '',   '',   ''],
            ],
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['A', 'C'],
                        ['A', 'D'],
                        ['A', 'E'],
                        ['A', 'F']
                    ], {
                        'A': 10,
                        'B': 10,
                        'C': 10,
                        'D': 10,
                        'E': 10,
                        'F': 10
                    },
                        'A', ['B', 'C']],
            "answer": 20,
            "explanation": [
                "Node A is in the center of network. Since the message goes from this node only crashed nodes didn't get a message.",
                ['',  '',  '',   '',   '',
                 '',  '',  'B',  '',   '',
                 '',  'F', 'A',  'C',  '',
                 '',  '',  'E',  'D',  '',
                 '',  '',   '',  '',   ''],
            ],
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'C'],
                        ['C', 'D']
                    ], {
                        'A': 10,
                        'B': 20,
                        'C': 30,
                        'D': 40
                    },
                        'A', ['A']],
            "answer": 100,
            "explanation": [
                "Nobody will get a mesage if node that sends emails is crushed",
                ['',  '',   '',   '',   '',
                 'A', '',   'C',  '',   '',
                 '',  'B',  '',   'D',  '',
                 '',  '',   '',   '',   '',
                 '',  '',   '',   '',   '']
            ],
        },
    ]
    for i, tst in enumerate(tests):
        print('Test number: ', i )
        assert disconnected_users(*tst["input"]) == tst['answer']
    print('Done. Try to check now. There are a lot of other tests')
