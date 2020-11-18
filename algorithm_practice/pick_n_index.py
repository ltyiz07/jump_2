def pick(m, n=0):
    if type(m) == int:
        m = [m]

    if n == 1:
        answer = [i for i in range(m - 1, -1, -1)]
        for i in answer:
            for k in m:
                k.append(i)
        return m

    for i in range



print(pick(9, 3))
