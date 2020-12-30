from morning.file_reader import read_lines


def valley(lst):
    size = int(lst[0])
    val = [list(map(int, l.split())) for l in lst[1:]]
    face = [[0] * size for _ in range(size)]

    # g_print(face)
    # algo start
    temp = 0
    for i in range(size-1, -1, -1):
        temp += val[-1][i]
        face[-1][i] = temp

    temp = 0
    for i in range(size-1, -1, -1):
        temp += val[i][-1]
        face[i][-1] = temp

    for h in range(size-2, -1, -1):
        for k in range(size-2, -1, -1):
            if face[h+1][k] <= face[h][k+1]:
                temp = val[h][k] + face[h+1][k]
            else:
                temp = val[h][k] + face[h][k+1]
            face[h][k] = temp
    # algo to here
    # g_print(face)

    return face[0][0]


def g_print(lst):
    for l in lst:
        for i in l:
            size = 3 - len(str(i))
            print(str(i) + " " * size, end=" ")
        print()

    print()


# dfs 방식을 했을때의 연산해야하는 모든 경우의 수.
def dfs_kind(n):
    if n == 0:
        return 0
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        grid[0][i] = 1
    for i in range(n):
        grid[i][0] = 1
    for i in range(n-1):
        for j in range(n-1):
            grid[i+1][j+1] = grid[i+1][j] + grid[i][j+1]
    return grid[-1][-1]


def valley2(lst):
    size = int(lst[0])
    val = [list(map(int, l.split())) for l in lst[1:]]
    temp1, temp2 = 0, 0
    for i in range(size):
        val[0][i] += temp1
        val[i][0] += temp2
        temp1, temp2 = val[0][i], val[i][0]

    for i in range(1, size):
        for j in range(1, size):
            val[i][j] += min(val[i-1][j], val[i][j-1])

    return val[-1][-1]


def valley3(lst):
    size = int(lst[0])
    val = [list(map(int, l.split())) for l in lst[1:]]

    def dfs(*pos):
        x, y = pos[0], pos[1]
        if pos == (size, size):
            return val[size][size] + min(val[y-1][x], val[y][x-1])
        else:
            if y == 0:
                if x == 0:
                    dfs(x + 1, y)
                elif x != 0:
                    if x == size:
                        dfs(0, y + 1)
                    else:
                        val[y][x] += val[y][x-1]
                        dfs(x + 1, y)
            else:
                if x == 0:
                    val[y][x] += val[y-1][x]
                    dfs(x+1, y)
                elif x == size:
                    val[y][x] += min(val[y-1][x], val[y][x-1])
                    dfs(0, y+1)
                else:
                    val[y][x] += min(val[y-1][x], val[y][x-1])
                    dfs(x+1, y)

    dfs(0, 0)
    return val[-1][-1]







if __name__ == "__main__":
    import timeit

    # print(valley(read_lines("./example_files/계곡탈출in3.txt")))
    # print(valley2(read_lines("./example_files/계곡탈출in3.txt")))
    print(valley3(read_lines("./example_files/계곡탈출in1.txt")))



    # print(dfs_kind(50))

map