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
    #
    # count = 0
    # lenth = 0
    # while len(keeping_box) != lenth or count == 0:
    #     for i in range(len(keeping_box)):
    #         lenth = len(keeping_box)
    #         if keeping_box[i] == keeping_box[i - 1] and i > 0:
    #             count += 1
    #             del keeping_box[i-1:i+1]
    #             break
    #
    # answer = count * 2
    # print(answer)
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
