def file_reader(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        answer = []
        for i in range(n):
            answer.append(list(map(int, f.readline().split())))
    return answer


def grid_max_added(lst):
    n = len(lst)
    max_lst = []
    for h_l in lst:
        temp_max = 0
        for h in h_l:
            temp_max += h
        max_lst.append(temp_max)
    print(max_lst)
    for v in range(n):
        temp_max = 0
        for k in range(n):
            temp_max += lst[k][v]
        max_lst.append(temp_max)
  d
    temp_max = 0
    for v in range(n):
        temp_max += lst[v][v]
    max_lst.append(temp_max)
    temp_max = 0
    for v in range(n):
        temp_max += lst[v][-v - 1]
    max_lst.append(temp_max)
    return max(max_lst)


def grid_max_added1(lst):
    n = len(lst)
    result = 0
    for i in range(n):
        garosum = serosum = 0
        for j in range(n):
            garosum += lst[i][j]
            serosum += lst[j][i]
        if garosum > result:
            result = garosum
        if serosum > result:
            result = serosum
    dagak1 = dagak2 = 0
    for i in range(n):
        dagak1 += lst[i][i]
        dagak2 += lst[i][n-1-i]
    if dagak1 > result:
        result = dagak1
    if dagak2 > result:
        result = dagak2
    return result


if __name__ == "__main__":
    print(grid_max_added(file_reader("example_files\\격자판최대합1.txt")))
    # print(grid_max_added(file_reader("example_files\\격자판최대합2.txt")))
    # print(grid_max_added1(file_reader("example_files\\격자판최대합1.txt")))
    # print(grid_max_added1(file_reader("example_files\\격자판최대합2.txt")))
