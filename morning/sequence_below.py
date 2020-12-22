from itertools import permutations


def reversed_pascal(n, m):
    first_lst = [i for i in range(1, n+1)]
    for per in permutations(first_lst):
        if below(per) == m:
            return per


def below(lst):
    length = len(lst)
    if length == 1:
        return lst[0]
    temp = []
    for i in range(length - 1):
        temp.append(lst[i] + lst[i+1])
    return below(temp)


if __name__ == "__main__":
    print(reversed_pascal(5, 61))
