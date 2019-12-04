def friday(day):
    from datetime import datetime
    _date = datetime.strptime(day, '%d.%m.%Y').date()
    day = _date.isoweekday()
    day = day if day <= 5 else day - 7
    return 5 - day

if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('11.11.1111') == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")
