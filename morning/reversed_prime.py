def reverse(n):
    answer = ""
    b = reversed(list(str(n)))
    for i in b:
        answer += i
    return int(answer)


def is_prime(m):
    if m < 2:
        return False
    elif m == 2:
        return True

    for i in range(2, m):
        if m % i == 0:
            return False
    else:
        return True


if __name__ == "__main__":
    a = [32, 55, 62, 3700, 250]
    for i in a:
        print(is_prime(reverse(i)))
