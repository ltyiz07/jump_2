def pick(m, n=0):
    if type(m) == int:
        m = [m]

    if n == 1:
        answer = [i for i in range(m - 1, -1, -1)]
        for i in answer:
            for k in m:
                k.append(i)
        return m


def pick02(m_l, n):
    answer = []
    if n == 1:
        for i in range(len(m_l)):
            for m in m_l:
                m += str(i)
                answer.append(m)


def pick03(lst, n):
    answer = []
    if n == 1:
        for ele in lst:
            last = int(ele[-1])
            for k in range(int(last) - 1, -1, -1):
                answer.append(ele + str(k))
        return answer
    for l in lst:
        last = int(l[-1])
        for k in range(int(last) - 1, 0, -1):
            answer.append(l + str(k))
    print(answer)
    return pick03(answer, n - 1)


def pick04(lst, n):
    answer = []
    if n == 1:
        for ele in lst:
            last = ele[-1]
            for k in range(last - 1, -1, -1):
                answer.append(ele[1:] + [k])
        return answer

    for el in lst:
        last = el[-1]
        for k in range(last - 1, 0, -1):
            answer.append(el + [k])
    return pick04(answer, n - 1)


def gen(m, n):
    return pick04([[m]], n)


if __name__ == "__main__":
    # print(pick04([[9]], 3))
    print(gen(4, 2))
    print(gen(4, 4))
    # print(gen(4, 1))
    # print(gen(4, 3))
    # print(pick(9, 3))
    # print(pick03(['9'], 3))
