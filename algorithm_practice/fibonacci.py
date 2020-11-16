def fibo(n):
    if n == 0:
        return 0
    return n + fibo(n-1)

print(fibo(6))