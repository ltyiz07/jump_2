def call(n, k):
    lst = [i for i in range(1, n+1)]
    k -= 1
    count = 0
    while len(lst) > 2:
        count += k
        out = count % len(lst)
        lst.pop(out)
    return lst[1]


def call1(n, k):
    lst = [i for i in range(1, n+1)]
    k -= 1
    while len(lst) > 1:
        for _ in range(k):
            lst.append(lst.pop(0))
        lst.pop(0)
    return lst


from collections import deque
def call3(n, k):
    dq = deque([i for i in range(1, n+1)])
    while len(dq) > 1:
        for _ in range(k-1):
            dq.append(dq.popleft())
        dq.popleft()
    return dq[0]



if __name__ == "__main__":
    print(call(8, 3))
    print(call(7, 2))
    print(call(10, 4))

    print("$" * 50)
    print(call1(8, 3))
    print(call1(7, 2))
    print(call1(10, 4))
    print(call1(20, 7))

    print("$" * 50)
    print(call1(8, 3))
    print(call1(7, 2))
    print(call1(10, 4))
