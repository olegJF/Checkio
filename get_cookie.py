def get_cookie(cookie, name):
    name = name + '='
    begin = cookie.find(name) + len(name)
    if begin < 0:
        return None
    end = cookie.find(';', begin)
    return cookie[begin: end] if end > 0 else cookie[begin:]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")
