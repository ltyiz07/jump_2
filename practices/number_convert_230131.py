def solution(x, y, n):
    """
    x to y
    possible operations:
        x += y
        x *= 2
        x *= 3
    """
    if x == y:
        return 0

    s = {x}
    count = 0
    while min(s) < y:
        t_s = s
        s = set()
        for v in t_s:
            s.add(v + n)
            s.add(v * 2)
            s.add(v * 3)
        count += 1
        if y in s:
            return count
    return -1


if __name__ == "__main__":
    assert solution(10, 40, 5) == 2
    assert solution(10, 40, 30) == 1
    assert solution(2, 5, 4) == -1
