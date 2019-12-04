def cut_sentence(line, length):
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if length >= len(line):
        return line
    res = ''
    if line[length-1] == ' ':
        res = line[:length-1]
    elif line[length] == ' ':
        res = line[:length]
    else:
        sep = line[:length].rfind(' ')
        if sep != -1:
            res = line[:sep]
               
    return res + '...'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 1) == "...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
