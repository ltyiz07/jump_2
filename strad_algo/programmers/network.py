def get_net(start, net):
    grid = net.copy()
    pool = set()
    pool.add(start)

    def dfs(target):
        grid[target][target] = 0
        if sum(grid[target]) == 0:
            return 
        else:
            for e, t in enumerate(grid[target]):
                if t == 1:
                    pool.add(e)
                    grid[target][e] = 0
                    grid[e][target] = 0
                    dfs(e)
    dfs(start)
    return pool


def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            visited = visited.union(get_net(i, computers))
            answer += 1

    return answer


if __name__ == "__main__":
    n, c = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print( solution(3, c) )
