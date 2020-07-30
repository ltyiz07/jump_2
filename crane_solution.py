def solution(board, moves):
    answer = 0
    keeping_box = []
    for m in moves:
        for j in range(len(board)):
            if not board[j][m - 1] == 0:
                keeping_box.append(board[j][m - 1])
                board[j][m - 1] = 0
                break
            else:
                pass
    print(keeping_box)


    count = 0
    for i in range(len(keeping_box)):
        if keeping_box[count] == keeping_box:

            answer += 1
        count += 1
    return answer


# solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
#          [1, 5, 3, 5, 1, 2, 1, 4])



# 보드 : board
# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 3],
#  [0, 2, 5, 0, 1],
#  [4, 2, 4, 4, 2],
#  [3, 5, 1, 3, 1]],


# 꺼냈으면 0으로 바꾸기
# 0 안나올때까지 계속 꺼내기
# 인덱스 갯수만큼 0이면 아무것도 하지 않기
# 문제 참조: https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3