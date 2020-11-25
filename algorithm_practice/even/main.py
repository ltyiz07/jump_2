from itertools import product
from itertools import combinations
import numpy as np


def solution(a):
    count = 0
    row = len(a)
    col = len(a[0])
    one_count = np.zeros(col, dtype=int)
    for l in a:
        for j, m in enumerate(l):
            if m == 1:
                one_count[j] += 1

    all_ = []
    for o in one_count:
        all_.append(combinations(range(row), o))
        print('*' * 50)
        for l in combinations(range(row), o):
            print(l)
    all_all = product(*all_)
    for l in all_all:
        temp_set = set()
        for m in l:
            temp_set = set(m).symmetric_difference(temp_set)
        if not temp_set:
            count += 1

    return count


if __name__ == "__main__":
    print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
    print('*' * 50)
    # solution([[1,0,0],[1,0,0]])
    print('*' * 50)
    # solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]])
