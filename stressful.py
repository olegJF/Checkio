
def is_stressful(subj):
    stress_words = ["help", "asap", "urgent"]
    if len(subj) >= 3 and subj[-3:].count('!') == 3:
        return True
    if all((l.istitle() for l in subj if l.isalpha())):
        return True
    words = subj.lower().split()
    for word in words:
        tmp = []
        for l in word:
            if not tmp:
                tmp.append(l)
            elif l.isalpha() and l != tmp[-1]:
                tmp.append(l)
        if ''.join(tmp) in stress_words:
            return True
    return False


if __name__ == '__main__':
    import sys
    # print(sys.argv)
    # assert is_stressful("Hi") == False, "First"
    # assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("We need you A.S.A.P.!!") == True, "Second"
    print('Done! Go Check it!')
    print(dir(is_stressful.__code__))
