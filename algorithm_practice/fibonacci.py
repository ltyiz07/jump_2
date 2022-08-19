def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n-1) + fibo(n-2)

def fibo2(n):
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    c = 0
    for i in range(n - 2):
        c = a + b
        b, a = c, b
    return c

if __name__ == "__main__":
    import time
    s = time.time()
    #print("answer1: ", fibo(35))
    e = time.time()
    print(f"duration: {e - s:.3f}")

    s = time.time()
    print("answer2: ", fibo2(10000))
    e = time.time()
    print(f"duration: {e - s:.3f}")
