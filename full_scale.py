from counter import deco_timer

def scaling(lst=[]):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        temp_lst = []
        for l in range(len(lst)):
            x = lst[l]
            xs = lst[:l] + lst[l+1:]
            for i in scaling(xs):
                temp_lst.append([x]+i)

        return temp_lst


a = ['a', 'b', 'c', 'd']
print(scaling(a))

from itertools import permutations

for i in permutations(a):
    print(i)