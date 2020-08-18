import timeit
start_time = timeit.default_timer()  # 시작 시간 체크

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
print(solution("29495098256098", 5))
print(solution("29495098256098", 5))
print(solution("29495098256098", 5))


end_time = timeit.default_timer()  # 종료 시간 체크
print('=' * 50)
print("%f초 걸렸습니다." % (end_time - start_time))