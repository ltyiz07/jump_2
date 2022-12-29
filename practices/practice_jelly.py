from itertools import permutations

def check_jelly(jelly_counter):
    m_jellies = max(jelly_counter.values())
    o_jellies = sum(jelly_counter.values()) - m_jellies
    return m_jellies > o_jellies
     

def solution(pouches):
    max_packs = len(pouches)
    pos_count = []

    j_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}
    for p in pouches:
        for l in p:
            j_count[l] += 1

    answer = 0 
    idxs = list(range(len(pouches)))

    def dfs(remain_idxs, remove_count=0):
        if len(remain_idxs) == 0:
            return 0
        for r_i in remain_idxs:
            for l in pouches[r_i]:
                j_count[l] -= 1
            if check_jelly(j_count):
                pos_count.append(remove_count + 1)
            co = remain_idxs.copy()
            co.remove(r_i)
            dfs(co, remove_count + 1)
            for l in pouches[r_i]:
                j_count[l] += 1

    dfs(idxs, 0)

    return max_packs - min(pos_count)


if __name__ == "__main__":
    answer = solution(["d", "a", "e", "d", "abdcc"])
    # answer = solution(["aabb", "baba"])
    print(answer)
