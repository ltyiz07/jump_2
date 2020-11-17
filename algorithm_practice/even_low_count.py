def solution(a):
    answer = -1
    row = len(a)
    col = len(a[0])
    row_ones = [0 for _ in range(col)]
    print(row_ones)

    for n, i in enumerate(a):
        for m, j in enumerate(i):
            if j == 1:
                row_ones[m] += 1
    print(row_ones)

    print(row, col)
    print(all_odds(row, row_ones))
    print('*' * 50)
    return answer


def all_odds(row, dices):
    """
    :param row: 열의 갯수
    :param dices: 각 열당 1의 갯수
    :return: 모든 경우의 수
    """
    answer = 1
    for d in dices:
        answer *= comb(row, d)
    return answer


def comb(n, m):
    """

    :param n: length of row
    :param m: number of '1'
    :return: all odds
    """
    a = 1
    for i in range(m):
        a *= n
        n -= 1
    return a

if __name__ == "__main__":
    print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
    print(solution([[1,0,0],[1,0,0]]))
    print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]))
