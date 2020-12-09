def solution(n):
    answer = ""
    l = ['4', '1', '2']
    while n >= 1:
        i = n % 3
        if i == 0:
            n = (n - 3) // 3
        else:
            n = n // 3
        answer += l[i]

    return answer[::-1]

if __name__ == "__main__":
    # print(solution(1))
    # print(solution(2))
    print(solution(3))
    # print(solution(4))
    # print(solution(5))
    # print(solution(6))


