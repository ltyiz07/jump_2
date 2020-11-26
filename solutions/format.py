def solution(s):
    answer_lst = []
    n = len(s) // 2
    LEN = len(s)
    ########################
    if LEN < 4:
        return LEN
    ########################
    for i in range(1, n + 1):
        fit = LEN // i + 1
        comp = ""
        temp_ans = LEN
        hit = 0
        for j in range(fit):
            if comp == s[i * j:i * (j + 1)]:
                if hit == 0:
                    temp_ans = temp_ans - i + 1
                    hit += 1
                else:
                    temp_ans -= i
                    hit += 1
                    if hit == 10:
                        temp_ans += 1
                    elif hit == 100:
                        temp_ans += 1
            else:
                hit = 0
            comp = s[i * j:i * (j + 1)]
        answer_lst.append(temp_ans)
    return min(answer_lst)


if __name__ == "__main__":
    print(solution("a" * 999))

