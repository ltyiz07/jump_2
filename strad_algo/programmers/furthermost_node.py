def solution(n, edge):
    answer = 0
    net = {e: set() for e in range(1, n+1)}
    for (v1, v2) in edge:
        net.get(v1).add(v2)
        net.get(v2).add(v1)
    
    search_target = {1} 
    visited = set()
    while len(visited) != n:
        answer = len(search_target)
        temp_nodes = set()
        for node in search_target:
            visited.add(node)
            temp_nodes.update(net.get(node))
        search_target = temp_nodes.difference(visited)
    return answer


if __name__ == "__main__":
    result = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
    print(f"{result} should be 3")
