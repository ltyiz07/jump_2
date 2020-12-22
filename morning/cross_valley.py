from morning.file_reader import read_lines


def valley(lst):
    size = int(lst[0])
    val = [list(map(int, l.split())) for l in lst[1:]]
    face = [[0] * size for _ in range(size)]

    g_print(face)
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
    g_print(face)

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

if __name__ == "__main__":
    # print(valley(read_lines("./example_files/계곡탈출in3.txt")))

    # math = []
    # for i in range(14):
    #     math.append(dfs_kind(i))
    # print(math)
    print(dfs_kind(50))
