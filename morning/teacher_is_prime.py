from math import sqrt
def is_prime(num):
    for j in range(2, int(sqrt(num) + 1)):
        if num % j == 0:
            return False
        return True

mul_prime = False
n = int(input("숫자 입력: "))
for i in range(2, int(sqrt(n) + 1)):
    if is_prime(i):
        m = n % i
        if m == 0 and is_prime(n // i):
            print("{} ==> {} * {}".format(n, i, n//i))
            mul_prime = True
            break
if not mul_prime : print("처리불가")