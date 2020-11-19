def dice(n, m):
    # if n == m:
        # return [n + 1]
    if n > m:
        return [(n + 1 - i) for i in range(n - m + 1)]
    else:
        return [(m + 1 - i) for i in range(m - n + 1)]


print(dice(8, 8))
print(dice(12, 20))
