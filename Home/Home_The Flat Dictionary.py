# -*- coding: utf-8 -*-
def flatten(dictionary):
    for keys in dictionary:
        print(keys)
    print(dictionary.keys())
    stack = [((), dictionary)]
    print('stack=',stack)
    result = {}
    while stack:
        path, current = stack.pop()
        print('path=',path,' current=',current)
        if current=={}:
            result["/".join((path))] = ""
        for k, v in current.items():
            print('k=',k,' v=',v)
            if isinstance(v, dict):
                stack.insert(0,(path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

print(flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                "job": "scout",
                "recent": {},
                "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}))


