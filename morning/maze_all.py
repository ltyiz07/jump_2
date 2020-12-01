from morning.file_reader import read_lines


def all_way(lst):
    maze = []
    for l in lst:
        if l:
            k = list(map(int, l.split()))
            maze.append(k)
    print(maze)

    dx = [0, 0, -1, +1]
    dy = [-1, +1, 0, 0]


def teachers_all_way(lst):
    maze = []
    matrix = [[0,0,0],
              [0,1,0],
              [0,0,0]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    l_index = len(matrix[0]) - 1

    cnt = 0

    def dfs(x, y):
        nonlocal cnt
        if x == l_index and y == l_index:
            cnt += 1
        else:
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx <= l_index and 0 <= yy <= l_index and matrix[xx][yy] == 0:
                    matrix[xx][yy] = 8
                    beautiful_print(matrix)
                    dfs(xx, yy)
                    matrix[xx][yy] = 0
        beautiful_print(matrix)
    matrix[0][0] = 8
    dfs(0, 0)


def beautiful_print(matrix):
    for xx in matrix:
        print(xx)
    print()
if __name__ == "__main__":
    all_way(read_lines("example_files\\미로경로수in1.txt"))
    print(teachers_all_way("example_files\\미로경로수in1.txt"))
