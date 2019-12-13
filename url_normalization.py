"""
    1. Converting the scheme and host to lower case.
    HTTP://www.Example.com/ → http://www.example.com/

    2. Capitalizing letters in escape sequences. All letters within a
    percent-encoding triplet (e.g., "%3B") are case-insensitive, and should be
    capitalized.
    http://www.example.com/a%c2%b1b → http://www.example.com/a%C2%B1b

    3. Decoding percent-encoded octets of unreserved characters.
    For consistency, percent-encoded octets in the ranges of
    ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E),
    underscore (%5F), or tilde (%) should not be created by Uniform Resource
    Identifiers (URI) producers and, when found in a URI, should be decoded to
    their corresponding unreserved characters by URI normalizers.
    http://www.example.com/%7Eusername/ → http://www.example.com/~username/

    4. Removing the default port. The default port (port 80 for the “http”
    scheme) should be removed from a URL.
    http://www.example.com:80/bar.html → http://www.example.com/bar.html

    5. Removing dot-segments. The segments “..” and “.” can be removed from
    a URL according to the algorithm described in RFC 3986
    (or a similar algorithm). ".." is a parent directory, "."
    is the same directory.
    http://www.example.com/a/b/../c/./d.html → http://www.example.com/a/c/d.html
"""
import re
punctuation = ['2D', '2E', '5F', '7E']
ALNUM = [i for i in range(int('30', 16), int('39', 16) + 1)]
ALNUM.extend([i for i in range(int('41', 16), int('5a', 16) + 1)])
ALNUM.extend([i for i in range(int('61', 16), int('7a', 16) + 1)])
ALNUM.extend([int(i, 16) for i in punctuation])


def checkio(url):
    if ':80' in url:
        if ':8080' in url:
            pass
        else:
            url = url.replace(':80', '')
    url = url.lower()
    matches = re.findall(r'%\w{2}', url)
    if matches:
        for octet in matches:
            dec = int(octet.replace('%', ''), 16)
            if dec in ALNUM:
                if 65 <= dec <= 90:
                    dec += 32
                url = url.replace(octet, chr(dec))
            else:
                url = url.replace(octet, octet.upper())
    matches = re.findall(r'\/\w+\/\.{2}\/', url)
    if matches:
        for match in matches:
            url = url.replace(match, '/')
    matches = re.findall(r'\/\w+\/\.{2}', url)
    if matches:
        for match in matches:
            url = url.replace(match, '')
    url = url.replace('./', '')
    return url


if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    assert checkio("http://example.com:80/HOME/../././Guest/1/../2/..") == "http://example.com/guest", "6th rule"
    assert checkio("http://Www.Checkio.org:80/ta%73K%2d/1/../2/./%3f%3e") == "http://www.checkio.org/task-/2/%3F%3E", "7th rule"
    print('OK')
