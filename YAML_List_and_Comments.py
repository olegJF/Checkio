
def yaml(text):
    def value_verification(_val):
        _val = _val.strip() if _val else _val
        if not _val or _val == 'null':
            return None
        if _val in ('true', 'false'):
            return True if _val == 'true' else False
        elif '"' in _val:
            _val = _val.replace('\\"', '*').replace('"', '').replace('*', '"')
        return int(_val) if _val.isdigit() else _val

    def list_value_verification(_val):
        if '"' in _val:
            _val = _val.replace('\\"', '*').replace('"', '').replace('*', '"')
            return _val
        if '#' in _val:
            indx = _val.find('#')
            _val = _val[:indx].strip()
        _val = int(_val) if _val.isdigit() else _val
        return _val if _val else None

    text_lst = [pair for pair in text.split('\n') if pair]
    yaml_dct = {}
    yaml_lst = []
    for pair in text_lst:
        if ':' in pair:
            key, val = pair.split(':')
            key = key.strip()
            val = value_verification(val)
            yaml_dct[key] = val
        else:
            if pair.startswith('#'):
                continue
            pair = pair.replace('-', '')
            pair = pair.strip()
            val = list_value_verification(pair)
            yaml_lst.append(val)

    return yaml_dct if yaml_dct else yaml_lst


if __name__ == '__main__':
    print("Example:")
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ['write some',
                                                         'Alex Chii', 89]
    assert yaml('# comment\n'
                '- write some # after\n'
                '# one mor\n'
                '- "Alex Chii #sir "\n'
                '- 89 #bl') == ['write some', 'Alex Chii #sir ', 89]
    assert yaml('- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5') == [1, 2, 3, 4, 5]
    assert yaml('-\n-\n-\n- 7') == [None, None, None, 7]

    tests = [

    ]
    for i, t in enumerate(tests):
        assert yaml(t['input'][0]) == t["answer"], i

    print("Coding complete? Click 'Check' to earn cool rewards!")
