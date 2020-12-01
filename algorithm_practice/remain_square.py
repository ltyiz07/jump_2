def solution(w, h):
    answer = w * h
    if w == 1 or h == 1:
        return 0
    if w >= h:
        big, small = w, h
    else:
        big, small = h, w

    common = 0
    for r in range(small, 0, -1):
        if big % r == 0 and small % r == 0:
            common = r
            break
    print(common)
    if small // common == 2:
        return (big // common) + 1
    x = big // common
    broken = ((x - 2) * 2 + 2) * (common)
    print(broken)
    print()
    return answer - ((x - 2) * 2 + 2) * common


def solution2(w, h):
    answer = w * h
    broken = 0
    if w == h:
        return answer - h
    elif w > h:
        big, small = w, h
    else:
        big, small = h, w
    for i in range(1, small + 1):
        broken += big // small
    return answer - broken

if __name__ == "__main__":
    print(solution(8, 12))
    print(solution(13, 12))
    print(solution2(10, 12))
    print(solution2(8, 14))
