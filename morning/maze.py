from morning import file_reader
from collections import deque


def short_out(lst):
    maze = []
    for l in lst:
        if l:
            k = list(map(int, l.split()))
            maze.append(k)


def teachers_short_out(lst):
    matrix = [[0, 0, 0, 1, 1],
              [0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dis = [[0] * 5 for _ in range(5)]
    que = deque()
    que.append((0, 0))
    matrix[0][0] = 1
    while que:
        print(que)
        temp = que.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if 0 <= x < 5 and 0 <= y < 5 and matrix[x][y] == 0:
                matrix[x][y] = matrix[temp[0]][temp[1]] + 1
                que.append((x, y))
    if matrix[4][4] == 0:
        print(-1)
    else:
        print(matrix[4][4] - 1)
    for m in matrix:
        print(m)


def beauti(lst):
    for l in lst:
        print(l)


if __name__ == "__main__":
    short_out(file_reader.read_lines("example_files\\미로탈출in1.txt"))

    teachers_short_out([])
