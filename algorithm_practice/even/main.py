from itertools import product
from itertools import combinations
import numpy as np
from math import comb


def solution(a):
    count = 0
    row = len(a)
    col = len(a[0])
    one_count = np.zeros(col, dtype=int)
    for l in a:
        for j, m in enumerate(l):
            if m == 1:
                one_count[j] += 1
    print("one_count: ", one_count)

    all_ = []
    comb_lst = []
    for o in one_count:
        comb_lst.append(comb(row, o))
    large = max(comb_lst)
    large_index = comb_lst.index(max(comb_lst))
    print(large, "   ", large_index)

    for i, o in enumerate(one_count):
        if i == large_index:
            all_.append((tuple(i for i in range(one_count[large_index])),))
            continue
        all_.append(tuple(combinations(range(row), o)))
    print(all_)

    all_all = tuple(product(*all_))
    print(all_all)
    for l in all_all:
        temp_set = set()
        for m in l:
            if not m:
                continue
            temp_set = set(m).symmetric_difference(temp_set)
        if not temp_set:
            count += 1
    count *= large
    count = count % (10 ** 7 + 19)

    return count


if __name__ == "__main__":
    # print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
    # print('*' * 50)
    # solution([[1,0,0],[1,0,0]])
    print('*' * 50)
    print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]))
