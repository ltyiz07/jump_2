# algorithm_practice.pick_n_set.py

def pick_n(lst=[], n=0):
    if n == 1:
        l = []
        for i in lst:
            l.append([i])
        return l

    else:
        temp_lst = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[i+1:]
            for r in pick_n(xs, n-1):
                temp_lst.append([x] + r)
        return temp_lst


def pick_all(lst=[] , n=0):
    temp_lst = []
    k = len(lst)
    for j in range(1, k+1):
        temp_lst += (pick_n(lst, j))
    return temp_lst


a = 'ab'
n = 2
print(pick_all(a))

# pick(a, 2)
