for i in range(10):
    print("hello")

def tri(n):
    if n == 0:
        return 3
    for i in range(tri(n-1)):
        n += 3
    return n

print(tri(3))

