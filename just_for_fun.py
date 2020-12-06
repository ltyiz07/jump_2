"""
자료형.
int 숫자.
str 문자.
list() ==> []
tuple() ==> ()
set() = {}
dict() = dict{}


변수로는 if, for ,int, str, list, tuple, set, dict,  등의 이미지정된 변수는 사용하면 안된다.

"""
answer = ""

a = ["apple", "pineapple", "grape", "seed"]



print("-".join(a))


def solution(numbers):
    answer = ""
    list1 = list(map(make, numbers))
    list1 = list(sorted(list1, reverse=True))
    latch = False
    print(list1)
    for e in range(len(list1) - 1):
        if float(list1[e]) == float(list1[e + 1]):
            answer += list1[e+1][2:]
            answer += list1[e][2:]
            latch = True
        elif latch:
            latch = False
            continue
        else:
            answer += list1[e][2:]
    print(answer)

    return answer


def make(n):
    length = len(str(n))
    n = str(int(n) / (10 ** length))
    while length + 2 > len(n):
        n += '0'
    return str(n)



from itertools import permutations


def solution1(numbers):
    a = permutations(numbers)
    answer_list = []
    for i in a:
        temp = ""
        for j in i:
            temp += str(j)
        answer_list.append(int(temp))

    return str(max(answer_list))

from itertools import permutations
def solution2(numbers):
    answer_lst = list(map(str, numbers))
    answer_lst = sorted(answer_lst, reverse=True)
    print(answer_lst)
    for e, i in enumerate(answer_lst):
        if len(i) == 1:
            for k in range(e):
                if len(answer_lst[k]) > 1 and int(answer_lst[k][1]) < int(i):
                    answer_lst.insert(k, answer_lst.pop(e))
                    break

    return "".join(answer_lst)
print(solution2([3, 30, 30, 3, 5, 9, 0, 32, 35]))
