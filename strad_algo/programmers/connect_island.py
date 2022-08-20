def gprint(grid):
    for g in grid:
        print(g)

def get_min(array):
    no_zero = [v for v in array if v != 0]
    if len(no_zero) == 0:
        return None
    else:
        return min(no_zero)

def get_grid(n, costs):
    grid = [[0] * n for _ in range(n)]
    for (a, b, cost) in costs:
        grid[a][b] = cost
        grid[b][a] = cost
    return grid
    

def solution(n, costs):
    answer = 0
    net = get_grid(100, costs)
    connected = {0}
    while len(connected) != n:
        price_node = set()
        for search_node in connected:
            min_price = get_min(net[search_node])
            if min_price is None:
                continue
            min_node = net[search_node].index(min_price)
            price_node.add((min_price, search_node, min_node))
        target_price_node = min(price_node, key=lambda x: x[0])
        answer += target_price_node[0]
        net[target_price_node[1]][target_price_node[2]] = 0
        net[target_price_node[2]][target_price_node[1]] = 0
        connected.add(target_price_node[2])
        for c_node in connected:
            net[c_node][target_price_node[2]] = 0
            net[target_price_node[2]][c_node] = 0
    return answer


def ancestor(node, parents):
    print(node, parents)
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution_2(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer

if __name__ == "__main__":
    a = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
    # a = solution_2(7, [ [2,3,7],[3,6,13],[3,5,23],[5,6,25],[0,1,29],[1,5,34],[1,2,35],[4,5,53],[0,4,75] ])
    print(a)
