def solution(v):
    answer = []

    v_x = v[0][0]
    v_y = v[0][1]
    if v_x == v[1][0] or v_x == v[2][0]:
        if v_x == v[1][0]:
            answer.append(v[2][0])
        else:
            answer.append(v[1][0])
    else:
        answer.append(v_x)

    if v_y == v[1][1] or v_y == v[2][1]:
        if v_y == v[1][1]:
            answer.append(v[2][1])
        else:
            answer.append(v[1][1])
    else:
        answer.append(v_y)

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))
