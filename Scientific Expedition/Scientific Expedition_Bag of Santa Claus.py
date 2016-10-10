from random import random, randint, uniform
tmp = 0
def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    global tmp
    if gift_number==1:
        tmp = current_gift
    third = int(gifts_in_bag//2.7)
    if gift_number<third:
        if tmp < current_gift: tmp = current_gift
    else:
        if tmp < current_gift: return True
        return False
    return False
   
    

RET={}
scale = (random() + random()) ** randint(0, 100)
standings = gift_count = best_gifts = 0
bag_count = 200
for i in range(bag_count):
    gifts_in_bag = randint(10, 100)
    gift_count += gifts_in_bag
    gifts = []
    selected_gift = None
    for i in range(gifts_in_bag):
        new_gift = uniform(0., scale)
        gifts.append(new_gift)
        decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
        if decision:
            
            selected_gift = new_gift
            gifts.extend([uniform(0., scale) for _ in range(gifts_in_bag - i - 1)])
            break
    if selected_gift is None:
        #print('len')
        priority = len(gifts)
    else:
        #print('selected_gift', selected_gift)
        #print(gifts)
        priority = sum(selected_gift < x for x in gifts)
        #print('else')
    standings += priority
    best_gifts += not priority
    #print(priority)
RET['code_result'] = best_gifts, bag_count, gift_count
print(RET)