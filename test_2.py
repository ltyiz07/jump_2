from itertools import permutations

a = ['a', 'b', 'c', 'e']
# b = permutations(a, 2)
# for i in b:
#     print(i)


c = set()
c |= {'f', 'e'}

print(c)

for i inmap(c, a)

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

