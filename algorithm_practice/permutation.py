# from itertools import permutations
def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm1(xs):
                l.append([x] + p)

        return l


data = ['a', 'b', 'c']

count = 0
print(perm1(data))

print(count)
