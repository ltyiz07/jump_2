import collections


def get_travel(graph, depart="ICN"):
    graph = graph.copy()
    answer = []

    def dfs(s):
        while graph[s]:
            dfs(graph[s].pop())
        if not graph[s]:
            answer.append(s)
            return
    dfs(depart)
    return answer[::-1]


def solution(tickets):
    graph = collections.defaultdict(list)
    for f, t in tickets:
        graph[f].append(t)
    [v.sort(reverse=True) for v in graph.values()]
    print(graph)
    return get_travel(graph)


if __name__ == "__main__":
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ICN"], ["SFO", "ATL"], ["ATL", "SFO"]]))
    # print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
