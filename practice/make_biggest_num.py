import timeit

def solution(number, k):
    count = 0
    while k != 0:
        if number[count + 1] > number[count]:
            number = number[0:count] + number[count + 1:]
            k -= 1
            count = 0
        else:
            count += 1
    return number

print(solution("1231234", 3))
print(solution("4177252841", 4))

print(timeit.timeit(solution(solution("1231234", 3))))