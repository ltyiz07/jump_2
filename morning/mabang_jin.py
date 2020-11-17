def odd_metrics(n):
    metric = [[0 for _ in range(n)] for _ in range(n)]

    print(metric)

def ma(metric):
    n = len(metric)

    if n % 2 == 0:
        print("not good")
        return "not good"

    move_normal = (-1, +1)
    move_down = (+1, 0)

    while True:
        pass


def teacher_ma():
    import numpy as np
    n = int(input(" n * n 마방진을 위한 n값을 입력(3이상, 홀수만) ="))
    matrix = np.zeros((n, n), dtype=int)

    s_row = 0; s_col = n//2
    matrix[s_row, s_col] = 1
    row = 0; col = 0

    for i in range(2, n*n + 1):
        row = s_row
        col = s_col

        s_row = s_row - 1; s_col = s_col + 1
        if s_row < 0:
            s_row = n + 1
        if s_col > n - 1:
            s_col = 0

        if matrix[s_row, s_col] == 0:
            matrix[s_row, s_col] = i
        else:
            s_row = row + 1; s_col = col
            matrix[s_row, s_col] = i


if __name__ == "__main__":
    odd_metrics(5)

    teacher_ma()