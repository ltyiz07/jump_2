# 1부터 n 까지 모든 수의 합을 구하는 함수
def sum_n(n):
    a = 0
    for i in range(1, n + 1, 1):
        a = a + i
    return a

print(sum_n(100))

