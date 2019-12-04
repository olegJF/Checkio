def checkio(text):
    begin = text.find('$')
    while begin != -1:
        end = text.find(' ', begin)
        if end < 0:
            end = len(text)
        tmp = text[begin: end]
        if tmp[-1] == '.' or tmp[-1] == ',':
            tmp = tmp[:-1]
        if len(tmp) > 3 and tmp[-3] == ',':
            new_tmp = tmp[:-3].replace('.', ',')
            tmp = new_tmp + '.' + tmp[-2:]
        elif  len(tmp) > 3 and tmp[-3] == '.' and tmp[:-3].count('.') == 0:
            pass
        else:
            tmp = tmp.replace('.', ',')
        text = text[:begin] + tmp + text[begin + len(tmp):]
        begin = text.find('$', begin + 1)
    return text


if __name__ == '__main__':    

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
