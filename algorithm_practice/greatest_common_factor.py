def greatest_common_factor(x, y):
    if x <= y:
        a = x
        b = y
    else:
        b = x
        a = y
    # b >= a
    if b % a == 0:
        return a
    else:
        for i in range(a - 1, 1, -1):
            if a % i == 0:
                if b % i == 0:
                    return i
        else:
            return 1

print(greatest_common_factor(6, 21))

def gcd(x, y):
    i = min(x, y)
    for n in range(i, 0, -1):
        if x % n == 0 and y % n == 0:
            return n

print(gcd(90, 1))

