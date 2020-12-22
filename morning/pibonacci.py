def pibo1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n + pibo1(n-1)


def pibo2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    temp = 0
    for i in range(n):
        temp += i
    return temp


if __name__ == "__main__":
    import timeit

    start1 = timeit.timeit()
    print(pibo1(50))
    print(timeit.timeit() - start1)

    start2 = timeit.timeit()
    print(pibo2(50))
    print(timeit.timeit() - start2)
