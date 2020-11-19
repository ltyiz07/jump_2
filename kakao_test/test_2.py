def pick_n(lst="", n=0):
    if n == 1:
        l = []
        for i in lst:
            l.append(i)
        return l

    else:
        temp_lst = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[i + 1:]
            for r in pick_n(xs, n - 1):
                temp_lst.append(x + r)
        return temp_lst

def solution(orders, course):
    list_n = []
    answer_set = set()
    for e, o in enumerate(orders):
        k = list(o)
        k.sort()
        orders[e] = ''.join(k)

    for c in course:
        list_n.append([])
        for o in orders:
            list_n[-1].extend(pick_n(o, c))
    for l in list_n:
        print('l=', l)
        list_count = []
        for i in l:
            list_count.append(l.count(i))
        print("list_count=", list_count)
        if l:
            if max(list_count) > 1:
                for e, k in enumerate(list_count):
                    if k == max(list_count):
                        answer_set.add(l[e])

    answer = list(answer_set)
    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))