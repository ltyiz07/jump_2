from morning.file_reader import read_lines as read


def banana(lst):
    box = []
    for l in lst[1:-1]:
        box.append(list(map(int, l.split())))
    print(box)

    x_ = [0, 0, 1, -1]
    y_ = [1, -1, 0, 0]
    day = 0

    def days(inbox):
        nonlocal day
        max_x = len(inbox)
        max_y = len(inbox[0])
        latch = True
        while latch:
            day += 1
            for i in range(max_x):
                for j in range(max_y):
                    if inbox[i][j] == 2:
                        inbox[i][j] = 1
                    if inbox[i][j] == -1:
                        latch = True
            if latch:
                for x, b in enumerate(inbox):
                    for y, l in enumerate(b):
                        if l == 1:
                            for i in range(4):
                                dx = x + x_[i]
                                dy = y + y_[i]
                                if 0 <= dx < max_x and 0 <= dy < max_y:
                                    if inbox[dx][dy] == -1:
                                        inbox[dx][dy] = 2
    days(box)
    beauti_print(box)

    return day


def banana2(lst):
    from collections import deque
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    col, row = tuple(map(int, lst[0].split()))
    matrix = [list(map(int, b.split())) for b in lst[1:-1]]
    beauti_print(matrix)
    chk_tbl = [[0] * col for _ in range(row)]
    Q = deque()
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                Q.append((i, j))
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                chk_tbl[nx][ny] = chk_tbl[x][y] + 1
                Q.append((nx, ny))
    beauti_print(chk_tbl)




def beauti_print(box):
    for b in box:
        print(b)


if __name__ == "__main__":
    print(banana2(read("./example_files/바나나숙성in1.txt")))
    # print(banana(read("./example_files/바나나숙성in2.txt")))
