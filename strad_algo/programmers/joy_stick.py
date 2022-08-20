def dist_from_a(alphabet):
    ans = ord(alphabet.lower()) - ord("a")
    if ans > 13:
        ans = 26 - ans
    return ans

def solution(name):
    ans_lst = []
    name = name.lower()
    up_down = 0
    for c in name:
        up_down += dist_from_a(c)
    if up_down == 0:
        return 0

    max_a_dist = 0
    max_a_start = 0
    max_a_end = 0
    temp_a_dist = 0
    temp_a_start = 0
    temp_a_end = 0
    last_a_dist = 0
    for e, c in enumerate(name):
        if c == "a":
            if temp_a_dist == 0:
                temp_a_start = e
            temp_a_end = e
            temp_a_dist += 1
            if e == len(name) - 1:
                last_a_dist = len(name) - temp_a_start
        else:
            temp_a_dist = 0
        if max_a_dist < temp_a_dist:
            max_a_dist = temp_a_dist
            max_a_start = temp_a_start
            max_a_end = temp_a_end

    ans_lst.append(len(name) - 1 - last_a_dist + up_down)
    if max_a_end != 0:
        ans_lst.append(2 * max_a_start - max_a_end + len(name) - 3 + up_down)
        ans_lst.append(2 * (len(name) - max_a_start) - (len(name) - max_a_end) + len(name) - 3 + up_down)
        ans_lst.append(2 * (len(name) - max_a_end) - (len(name) - max_a_start) + len(name) - 3 + up_down)
    print(ans_lst)
    return min(ans_lst)


if __name__ == "__main__":
    ans = solution("JEROEN")
    print(f"{ans} should be 56")
