from collections import OrderedDict


def frequency_sorting(numbers):
    unique_elem = set(numbers)
    if len(unique_elem) == len(numbers):
        return sorted(numbers)
    elem_more_one = {i: numbers.count(i) for i in unique_elem if 
                     numbers.count(i) > 1}
    elem_eq_one = sorted([i for i in unique_elem if numbers.count(i) == 1])
    values = list(elem_more_one.values())
    sorted_elem_more_one = OrderedDict()
    for v in sorted(list(set(values)), reverse=True):
        if values.count(v) > 1:
            t = {key: val for key, val in elem_more_one.items() if v == val}
            sorted_elem_more_one.update(OrderedDict(sorted(t.items())))
        else:
            sorted_elem_more_one.update({key: val for key, val in 
                                         elem_more_one.items() if v == val})
    tmp = []
    for k, v in sorted_elem_more_one.items():
        tmp.extend([k] * v)
    if elem_eq_one:
        tmp.extend(elem_eq_one)
    return tmp


if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
