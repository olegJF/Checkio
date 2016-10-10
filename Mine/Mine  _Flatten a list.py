def c(a):
  r=[]
  for i in a:
    if type(i)!= list: r.append(i)
    else: r += c(i)
  return r
print(c([1,2,3,[4,5],[6],7,8,[9,10]]))



import re

def flat_list(L):

    return map(int, re.findall(r'-?\d+', str(L)))

