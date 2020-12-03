from morning.file_reader import read_lines


def apple_farm_dfs(lst):
    n = int(lst[0])
    depth = n // 2
    farm = []
    for line in lst[1:-1]:
        farm.append(list(map(int, line.split())))

    answer = 0

    x_ = [1, -1, 0, 0]
    y_ = [0, 0, 1, -1]

    def harvest(x, y, d):
        print("x: ", x, "  y: ", y, "  d: ", d)
        nonlocal answer
        answer += farm[x][y]
        farm[x][y] = -1
        nice_print(farm)
        if d > 0:
            nice_print(farm)
            for i in range(4):
                temp_x = x + x_[i]
                temp_y = y + y_[i]
                if farm[temp_x][temp_y] > 0:
                    harvest(temp_x, temp_y, d - 1)
    harvest(depth, depth, depth)
    print(answer)
    return


def nice_print(lst):
    for i in lst:
        for j in i:
            print(f"{j:3}", end="")
        print()


if __name__ == "__main__":
    print(apple_farm_dfs(read_lines(".\\example_files\\apple_tree_1.txt")))
