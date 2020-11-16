import timeit
start_time = timeit.default_timer()  # 시작 시간 체크


def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm1(xs):
                l.append(x + p)
        return l


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


def pick_all(lst=""):
    temp_lst = []
    k = len(lst)
    for j in range(1, k+1):
        temp_lst += (pick_n(lst, j))
    return temp_lst

def solution(numbers):
    answer = 0
    temp_set = set(())
    picked_list = pick_all(numbers)
    for i in picked_list:
        for p in perm1(i):
            temp_set.add(int(p))
    temp_set.discard(0)
    temp_set.discard(1)
    if 2 in temp_set:
        temp_set.discard(2)
        answer += 1
    print(temp_set)
    for t in temp_set:
        temp_counter = 0
        for r in range(2, t):
            if t % r == 0:
                break
        else:
            answer += 1


    return answer

print(solution("0172"))


###################################################
end_time = timeit.default_timer()  # 종료 시간 체크
print('=' * 50)
print("%f micro sec 걸렸습니다." % ((end_time - start_time) * 1000000))