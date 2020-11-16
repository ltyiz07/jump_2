def solution(board, moves):
    answer = 0
    keeping_box = []
    count = 0
    for m in moves:
        for j in range(len(board)):
            if not board[j][m - 1] == 0:
                picked = board[j][m - 1]
                board[j][m - 1] = 0
                if count > 0:
                    if keeping_box[count - 1] == picked:
                        keeping_box.pop()
                        count -= 1
                        answer += 2
                    else:
                        keeping_box.append(picked)
                        count += 1
                else:
                    keeping_box.append(picked)
                    count += 1
                break
    print(keeping_box, count)

    return answer