# -*- coding: utf-8 -*-
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    list_args = args if len(args) > 1 else list(args[0])
    minimum = sorted(list_args)[0]
    if key:
        minimum_elem = key(list_args[0])
        minimum = list_args[0]
        for elem in list_args:
            if minimum_elem > key(elem):
                minimum = elem
                minimum_elem = key(elem)
    return minimum


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    list_args = args if len(args) > 1 else list(args[0])
    maximum = sorted(list_args)[-1]
    if key:
        maximum_elem = key(list_args[0])
        maximum = list_args[0]
        for elem in list_args:
            if maximum_elem < key(elem):
                maximum = elem
                maximum_elem = key(elem)
    return maximum


print(min(True, False, -1))
#if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert max(3, 2) == 3, "Simple case max"
    #assert min(3, 2) == 2, "Simple case min"
    #assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    #assert min("hello") == "e", "From string"
    #assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    #assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"


