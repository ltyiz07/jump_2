import copy
import sys
sys.setrecursionlimit(10**5)


def get_dfs(pos, maps, col, row):
    c, r = pos

    if c < 0 or c > col - 1 or r < 0 or r > row - 1:
        return 0

    if maps[c][r] == 'X':
        return 0
    else:
        temp = int(maps[c][r])
        maps[c] = maps[c][:r] + 'X' + maps[c][r+1:]
        return temp + \
        get_dfs([c+1, r], maps, col, row) + \
        get_dfs([c, r+1], maps, col, row) + \
        get_dfs([c-1, r], maps, col, row) + \
        get_dfs([c, r-1], maps, col, row)
        
    
def solution(maps):
    maps = copy.deepcopy(maps)
    answer = []
    for c, line in enumerate(maps):
        for r, val in enumerate(line):
            if maps[c][r] != 'X':
                max_date = get_dfs((c, r), maps, len(maps), len(maps[0]))
                answer.append(max_date)
    if len(answer) == 0: return [-1]
    return sorted(answer)

if __name__ == "__main__":
    assert solution(["X591X","X1X5X","X231X", "1XXX1"]) == [1, 1, 27]

