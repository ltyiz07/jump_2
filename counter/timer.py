import timeit
start_time = timeit.default_timer()  # 시작 시간 체크
###################################################

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
                l.append([x] + p)
        return l


data = ['2', '0', '1', '4']
permutations_set = set(())

for p in perm1(data):
    temp_str = ""
    for i in p:
        temp_str += str(i)
    permutations_set.add(int(temp_str))

###################################################
end_time = timeit.default_timer()  # 종료 시간 체크
print('=' * 50)
print("%f micro sec 걸렸습니다." % ((end_time - start_time) * 1000000))
