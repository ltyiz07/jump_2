from morning.file_reader import read_lines, print_2d


def block_count(lst):
    size = int(lst[0])
    town = []
    for l in lst[1:-1]:
        town.append(list(map(int, l.split())))
    count = 0
    print_2d(town)
    print()

    def plague(pos):
        x, y = pos[0], pos[1]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < size and 0 <= temp_y < size and town[temp_x][temp_y] == 1:
                town[temp_x][temp_y] = 8
                plague((temp_x, temp_y))

    for e, l in enumerate(town):
        for i, m in enumerate(l):
            if m == 1:
                plague((e, i))
                count += 1
                print_2d(town)
                print()
    return count





if __name__ == "__main__":

    # print(block_count(read_lines("example_files/town1.txt")))
    # print(block_count(read_lines("example_files/town2.txt")))
    # print(block_count(read_lines("example_files/town3.txt")))

    lines = read_lines("example_files/town1.txt")
    matrix = []
    n = int(lines[0])
    for i in lines[1:-1]:
        matrix.append(list(map(int, i.split())))
    print_2d(matrix)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(row, col, sep):
        global h_cnt
        h_cnt += 1
        matrix[row][col] = sep
        for i in range(4):
            nrow = row + dx[i]
            ncol = col + dy[i]
            if 0 <= nrow < n and 0 <= ncol < n and matrix[nrow][ncol] == 1:
                dfs(nrow, ncol, sep)
        print()
        print_2d(matrix)


    danji = []
    sep = 8
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                h_cnt = 0
                dfs(i, j, sep)
                danji.append(h_cnt)

    print(len(danji), sorted(danji))


