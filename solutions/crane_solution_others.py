def solution(board, moves):
    answer = 0
    keeping_box = []
    for m in moves:
        for j in range(len(board)):
            if board[j][m - 1] != 0:
                keeping_box.append(board[j][m - 1])
                board[j][m - 1] = 0
                if len(keeping_box) > 1:
                    if keeping_box[-1] == keeping_box[-2]:
                        keeping_box.pop()
                        keeping_box.pop()
                        answer += 2
                break
    print(answer)
    return answer
