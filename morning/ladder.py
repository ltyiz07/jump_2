from morning.file_reader import read_lines


def to_ladder(lst):
    ladder = []
    for l in lst[:-1]:
        ladder.append(list(map(int, l.split())))
    print(ladder)
    return ladder


def climbing(ladder, pos=(0,0)):
    if pos[1] == 9:
        return ladder[0].index(-1)
    elif pos[1] == 0:
        level = ladder[9].index(2)
        ladder
        climbing(ladder, pos[1]+1)

    for e, l in enumerate(ladder):
        level = e
        if -1 in l:
            level = l.index(-1)
    brint(level)





def climbing2(ladder):
    checker = [[0] * 10 for _ in range(10)]


def brint(lst2D):
    for l in lst2D:
        print(l)



if __name__ == "__main__":
    climbing2(to_ladder(read_lines("example_files/사다리in1.txt")))

    matrix = to_ladder(read_lines("example_files/사다리in1.txt"))
    checker = [[0] * 10 for _ in range(10)]

    def dfs(row, col):
        checker[row][col] = 1
        if row == 0:
            print(f"luck in {col}")
        else:
            if col - 1 >= 0 and matrix[row][col-1] == 1 and checker[row][col-1] == 0:
                dfs(row, col-1)
            elif col + 1 < 10 and matrix[row][col+1] == 1 and checker[row][col+1] == 0:
                dfs(row, col+1)
            else:
                dfs(row-1, col)

    for col in range(10):
        if matrix[9][col] == 2:
            dfs(9, col)

