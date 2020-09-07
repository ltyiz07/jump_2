import copy
def solution(numbers):
    answer = 0
    length = len(numbers)
    number_set = {}

    for l in range(length):
        temp_num = ""
        temp_numbers = copy.copy(numbers)
        temp_num[l] = temp_num.pop()
        for k in range(l):
            temp_num += "0"
            for n in numbers:
                pass

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



    return answer


# print(solution("17"))
solution("011")
#
# set_a = set(())
# set_a.add(34)
# set_a.add(int('034'))
# print(set_a)
