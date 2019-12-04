from collections import OrderedDict, Counter
from copy import deepcopy

MONSTERS = '''
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
'''


def halloween_monsters(spell: str)-> int:
    monsters_lst = [m for m in sorted(MONSTERS.split('\n')) if m]
    monsters_dct = OrderedDict()
    for monster in monsters_lst:
        monsters_dct[monster] = Counter(monster)
    spell_dct = Counter(spell)
    res = 0
    possible_monsters = [name for name, dct in monsters_dct.items() if
                         all(l in spell_dct for l in dct.keys())]
    tmp_res = []
    empty = False
    for i in range(len(possible_monsters)):
        if empty:
            break
        tmp = deepcopy(spell_dct)
        res = 0
        for name in possible_monsters:
            dct = monsters_dct[name]
            is_monster = all(dct[l] <= tmp[l] for l in dct.keys())
            while is_monster:
                res += 1
                tmp -= dct
                if not tmp:
                    empty = True
                    break
                is_monster = all(dct[l] <= tmp[l] for l in dct.keys())
        tmp_res.append(res)
        possible_monsters.append(possible_monsters.pop(0))
    return max(tmp_res)

# def halloween_monsters(spell):
#
#     maximum_monsters = []
#
#     def search(rest_spell, rest_monsters, monsters, num=0, max_num=0):
#
#         if not (rest_spell and rest_monsters):
#             if num > max_num:
#                 maximum_monsters.clear()
#             if num >= max_num:
#                 maximum_monsters.append(monsters)
#             return max(max_num, num)
#
#         name_monster = rest_monsters[0]
#         ct_monster = Counter(name_monster)
#         new_spell = deepcopy(rest_spell)
#         new_monsters = list(monsters)
#         while True:
#             max_num = search(new_spell, rest_monsters[1:], new_monsters, num, max_num)
#             if ct_monster - new_spell:
#                 break
#             new_spell -= ct_monster
#             new_monsters.append(name_monster)
#             num += 1
#
#         return max_num
#
#     result = search(Counter(spell), MONSTERS.split(), [])
#     return result, maximum_monsters and maximum_monsters[0]
#

if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    assert halloween_monsters('"fbwrvuadocsgvujmpotkhvqvrzfbadbwnhgxpadkqqztrbyinxwcipeqysumzgemlcaxjonzn"') == 6
    print("Your spell seem to be okay. It's time to check.")
