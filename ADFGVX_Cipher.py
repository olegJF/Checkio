from string import punctuation
title = list('ADFGVX')


def secret_dict(text, _decode=False):
    _dct = {}
    for i, val in enumerate(text):
        key = f'{title[i // 6]}{title[i % 6]}'
        if _decode:
            _dct[key] = val
        else:
            _dct[val] = key
    return _dct


def remove_doubles(word):
    doubles = [i for i in word if word.count(i) > 1]
    for ch in doubles:
        while word.count(ch) > 1:
            first = word.find(ch)
            second = word.find(ch, first + 1)
            word = word[:second] + word[second + 1:]
    return word


def encode(message, secret_alphabet, keyword):
    message = message.lower().replace(' ', '')
    for ch in punctuation:
        message = message.replace(ch, '')
    secret_dct = secret_dict(secret_alphabet)
    tmp_message = ''
    for ch in message:
        tmp_message += secret_dct[ch]
    # print(tmp_message)
    if len(set(keyword)) != len(keyword):
        keyword = remove_doubles(keyword)
    size = len(keyword)
    tmp_dct = {}
    for i, ch in enumerate(tmp_message):
        key = i % size
        tmp_dct.setdefault(key, '')
        tmp_dct[key] += ch
    # print(tmp_dct)
    srtd_keyword = sorted(list(keyword))
    tmp_message = ''
    for ch in srtd_keyword:
        tmp_message += tmp_dct[keyword.find(ch)]
    # print(tmp_message)
    return tmp_message


def decode(message, secret_alphabet, keyword):
    secret_dct = secret_dict(secret_alphabet, True)
    if len(set(keyword)) != len(keyword):
        keyword = remove_doubles(keyword)
    size = len(keyword)
    srtd_keyword = sorted(list(keyword))
    rows, remainder = divmod(len(message), size)
    # print(message)
    if remainder:
        rows += 1
        remainder_str = sorted(list(keyword[remainder - size:]))
        for ch in remainder_str:
            i = rows * srtd_keyword.index(ch) + (rows - 1)
            message = message[:i] + ' ' + message[i:]
    # print(message)
    tmp_dct = {}
    for i in range(size):
        key = i * rows
        tmp_dct.setdefault(srtd_keyword[i], '')
        tmp_dct[srtd_keyword[i]] += message[key: key + rows]
    # print(tmp_dct)
    tmp_message = ''
    for i in range(rows):
        for ch in keyword:
            tmp_message += tmp_dct[ch][i]
    tmp_message = tmp_message.strip()
    res = ''
    for i in range(0, len(tmp_message), 2):
        res += secret_dct[tmp_message[i: i+2]]
    return res


if __name__ == '__main__':

    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    #
    # assert decode("FXGAFVXXAXDDDXGA",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'iamgoing', "decode I am going"
    #
    # assert encode("attack at 12:00 am",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    #
    # assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'attackat1200am', "decode attack"
    #
    # assert encode("ditiszeergeheim",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    #
    # assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    #
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    #
    # assert decode("DXGAXAAXXVDDFGFX",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'iamgoing', "decode weasel == weasl"

    _TESTS = [
    [
        encode("One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0", "d9sr4qxvaz75yu2hkwpm8j63b1legot0ifnc", "monty"),
        'VGFFAGVGXGXVDVXGXVDGXDVAVXFVDXDFVVVAXGVXXVXXGGXAFDFADDFXVVGVVXXFGXDXDAAVGVVGFAGXVAFGVGAGVFGGXGFFXDAD'],
    [
        encode("Your highness, when I said that you are like a stream of bat\'s piss, I only mean that you shine out like a shaft of gold when all around it is dark", "xk4wre5o1l0fyhmja62n7qc8it9dsv3gzbpu", "python"),
        'DDDVDAADAVGXDVXDAAGXDDXADGXDDDGXGVDDGDXADVXVGVDVAVVFGVVDAVDAVDXAVVDDGDGDGAVXVGVAVVFDAVFAFXVVDFFFFVGXVFFDDAGDDVVFFAXAAGFVVXAAVADFXVGFGFDFAVAVDDDFFFXVVADFFVFVVFFFDAVFDVVVDAVVXVDDAFVXVADAGVVAAVDXGDVDDXXDVXDVVVDFDVDDXDDVXXGDVVXAVV'],
    [
        encode("I don\'t wanna talk to you no more, you empty headed animal food trough wiper! I fart in your general direction! You mother was a hamster and your father smelt of elderberries!", "chtqrlz0fxdj61wgesi5kya4n7uv93o2p8mb", "daily"),
        'AVFVFGAVAAGFFAVDAGFDVFFFAAAXVVVDVAAXVAVFDFVVGAVFXAAAVFVFGAFAAXXAXAGFXGGVVVDAAFFFGVGGAVAXAAXGXFAVAVFVGFGDFVXVFXAVDAGAGFGFXVXVADDVGVXVXGGVDVVAFAGVFFVAXDFXGXAAXVAVXXDXAVGXVAVGVAGVVFAXFFVGAAAAAAAAFAAVGFVGVGAVAFFGVAVDADFAVAFDVAAXFVVAFXAXVVVGVFVXXXFVDXVGFGFFVAAAAGFAVGVXFGVVFAVFFFVXVF'],
    [
        encode("My philosophy, like color television, is all there in black and white", "gxy3dft2qis8zljen0o4671kwabuhmc5r9vp", "checkio"),
        'VVGXFFFDFDFVDXFVVVDADDVDXGFXDDFVFVXFVFXVAXDGDAGVVDAFVDDAAXFGAGGXFDGDFFDFGADFGVVGAAGVGGDVGFAVVGXDAFXAFDGAVDGGDXVG'],
    [
        encode("Strange women lying in ponds distributing swords is no basis for a system of government!", "la159r6ng4vetycs20xfwzkdbp7ohquj8im3", "world"),
        'ADGVAGXDGXFGFDGXXDAGVDFXGGAVFADXXDXFVDGGXADGAGDAXDADDGVXXDGAFVXFDDGFGAAXFVXFGFGAGFVDVDXFDDGDDDDDGFXXGFGFGVGGXFAVFDDDFXDFDADGVXXAVADFGGVDFGFGXDDXDA'],
    [
        encode("We are no longer the knights who say ni! We are now the knights who say ekki-ekki-ekki-pitang-zoom-boing!", "3rktdiz9805hujnswgp16lfcvm2x4oqa7ybe", "ubermonty"),
        'VFFDXFDXFXXDGXXAXXXXFFXFVXXVXDXXXAXDVXXXXDXFDFFAXAFAGVXAGAFAXADAFFGAFADVXDGXAXVFAVFGFFAFXXAXVXXXDGXXAXVXAFAAVDVDFGFXXGAGXFAXFXFFXFGAGXVFXFVXXXAFDFXXAFFGFXDXFDAXGFVF'],
    [
        encode("Nudge, nudge, wink, wink. Know what I mean?", "ojc35lab407zsrqev1tkhp9yi6wu2gnxfd8m", "yep"),
        'AXXXGVGVAVAGDAFGAVXDAVGFAXXVAGFXDXAVFGAFAXGVGVGFFXDVAGAVFDAXGX'],
    [
        decode("DXDXDGVXFXDVVDXXXFAXXGDDGGDDGDAVDGFGGVVVFAVGGXFXADFAFXGXFAVGFXVXGVXGGVXFAGXFXAFVGFAFDXGFFFDVDGGFAFXX", "zm3ahs68ig9bc7xy4pu1jntvld2rk05oewfq", "yep"),
        'one1two2three3four4five5six6seven7eight8nine9zero0'],
    [
        decode("AAGAXFAAGDXFAFXFGAGAFAXDGAFFGAXFFXDXGFXXGAFDDDAGXDXDFADDGAGDFGGAGVXAFGFXAFFGVFFXAAGAGAFDDAFXGGDDFXDGADGAXGDADGGAAXAAAAXFVFDXXDFGAFXXVDADFFADDDVVGXFDAXDAVFDAGFGDXADDDADFGAVFAADGVAVFVXFFXFFAGFAAFFDFGFAFADADGDDFXFFADAVXAFXXDAFAFV", "noieqp9mbxhd7glswayr4f21kz5jc0ut8v36", "ubermonty"),
        'yourhighnesswhenisaidthatyouarelikeastreamofbatspissionlymeanthatyoushineoutlikeashaftofgoldwhenallarounditisdark'],
    [
        decode("FFGDXFFVFAGAVAVDFXFFGDGXAFVAVAXGGGVAGAADFFAFGVDXVFVFDXVFGDADGVGAVVFFVFAGXVGVDGAVGVGDVDXAXVGVVAADGXVVDFAAGVVXAGGGAGFXVGVAVVDDDVVAVVXVAVGAGFXGXVXGVFADXADAAGVADVVXVXAVXAVVAVAFVAFXFAGDVFXDFFFDXADXGVVVAFVFGVFDDVAVAVFXGAFXDXAAXVXVDVGXFVFVVAGVAAGADVAADDXDXVAAAXAXFVFFADDAVDVAADAAFAVFAA", "8a62srwhbzf3m04joquptxncegd1y97vki5l", "world"),
        'idontwannatalktoyounomoreyouemptyheadedanimalfoodtroughwiperifartinyourgeneraldirectionyoumotherwasahamsterandyourfathersmeltofelderberries'],
    [
        decode("XVFDGFGGFAAVGVAVVDGGXAVXAFFGXXGVFXAAVFDGGDDADXAAGVXXGVVFXDGFGFFVGXFAGFXGFDXAAAGADGAFAADGAXDGGADDGADGXDAGADAADDVA", "sc7nq45pw6d9ek3of8ylv2utz10harimxgjb", "checkio"),
        'myphilosophylikecolortelevisionisallthereinblackandwhite'],
    [
        decode("DFFXXXXDVFVVDDFXAFVFDVDGXFFDXFXFVADDVXADXDXFVDVXAFVFDFVXXAXGAAVDXFXDDFXXVFVFDDDGXXXXFAXDXDXFXDFXXDDDDDDVDDDDVFXAVXXFXVXAXGVDADAGVGXAXDXFVXAFXGVVXG", "hz1qwedb78inasg3km6l49ft52x0crpuvjoy", "daily"),
        'strangewomenlyinginpondsdistributingswordsisnobasisforasystemofgovernment'],
    [
        decode("AAVXFVXADGVFDGDGVAAAVVGDGVADDDAGDGVADAAVAAFGDVAAVADDXDFDAXADAAFDXXAXGAAFDXGDGDAXDAGADGXGAAFGFDADFFAFDDXGAFAAFXXXFADFFAFAGAADAAFXGDDVFDGGVFDDFAAFGDADDFVXADGVVAAFXDDX", "xothwv1nuzkfsa9y2gicrdm8q37p54e6j0lb", "python"),
        'wearenolongertheknightswhosayniwearenowtheknightswhosayekkiekkiekkipitangzoomboing'],
    [
        decode("FAFADVGXFXXDFAVAVGXFXDVGDVDVDXGDGAAGVVFVFVDDVFXADAXDXDFXGVDAXA", "a9uch1sq5rgwo6vyn73ilb8k4ef0xjdmptz2", "monty"),
        'nudgenudgewinkwinkknowwhatimean'],

    ]
    for t in _TESTS:
        res, et = t
        assert res == et

    print('OK!')
