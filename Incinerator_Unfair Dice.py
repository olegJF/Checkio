# -*- coding: utf-8 -*-

def enemy_lost(all_digit,my_dice):
    res = 0
    for i in my_dice: res +=all_digit[i]
    if res>0: return True
    return False

def winning_die(enemy_die):
    size = len(enemy_die)
    all_numbers = sum(enemy_die)
    if size == all_numbers: return []
    max_number = all_numbers-(size-2)
    all_digit = [i for i in range(max_number)]
    # all_digit [0,1,2,3,4,5,6] for enemy_die [2,3,3]
    my_dice = [1 for i in range(size-1)]
    my_dice.append(max_number-1)
    """
     the initial position of my_dice is [1,1,6] and
     sum(my_dice)== sum([2,3,3])
    """
    for i in range(len(all_digit)):
        res = 0
        for dgt in enemy_die:
            if i != 0:
                if dgt<i: res +=1
                elif dgt>i: res -=1
        all_digit[i] = res
    """
     all_digit is [0,-3,-2,1,3,3,3] for enemy_die [2,3,3]
    
        | 2 | 3 | 3 |
      1 |-1 |-1 |-1 | -3
      2 | 0 |-1 |-1 | -2
      3 | 1 | 0 | 0 |  1
      4 | 1 | 1 | 1 |  3
      5 | 1 | 1 | 1 |  3
      6 | 1 | 1 | 1 |  3
    
     the initial position of my_dice [1,1,6] loses to enemy_die [2,3,3]
     all_digit[1]+all_digit[1]+all_digit[6]=(-3)+(-3)+3 < 0
    """
    min_positiv_dgt, i = 0, 0
    while all_digit[i] <= 0: i+=1
    min_positiv_dgt = i
    if enemy_lost(all_digit,my_dice): return my_dice
    first_elem = size -(int(size//2) + 1)
    while my_dice[-1] >= min_positiv_dgt:
        """
         at each iteration decreases the value of the last item in the list
         and consistently increases the value for each element
         from [first_elem] to [len(my_dice)-2].
         And check out possibility to win.
        """
        
        for x in range(first_elem,size-1):
            my_dice[-1] -= 1
            my_dice[x] += 1
            #print(my_dice)
            if enemy_lost(all_digit,my_dice): return sorted(my_dice)
            if my_dice[-1] <min_positiv_dgt: break

    return []


print(winning_die([2, 4, 6, 8, 10, 12, 14, 16, 18]))

##for i in itertools.combinations_with_replacement(tmp, size):
##        if sum(i) == all_numbers:
##            if enemy_lost(all_digit,i):
##                return list(i)


