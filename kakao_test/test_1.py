def solution(new_id):
    answer = ''
    case_folded = new_id.casefold()
    for i, w in enumerate(case_folded):
        if 96 < ord(w) and ord(w) < 123:
            answer += w
        elif 47< ord(w) and ord(w) < 58:
            answer += w
        elif ord(w) == 45 or ord(w) == 95 or ord(w) == 46:
            answer += w
    while '..'in(answer):
        answer = answer.replace('..', '.')

    answer = answer.strip('.')
    if not answer:
        return 'aaa'
    answer = answer[:15]
    answer = answer.strip('.')
    while len(answer) < 3:
        answer += answer[-1]
    return answer

print(solution(".....abc........dep_-.........-_...."))
