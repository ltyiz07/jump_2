from morning.file_reader import read_lines


def packing(lst):
    kind = int(lst[0].split()[0])
    max_weight = int(lst[0].split()[1])
    print(kind, max_weight)
    weight_value = list(map(lambda x: (int(x.split()[0]), int(x.split()[1])), lst[1:]))
    print(weight_value)
    answer = []

    def dfs(cur_weight, cur_value):
        nonlocal weight_value
        if cur_weight < 0:
            return

        for weight, value in weight_value:
            if cur_weight - weight >= 0:
                answer.append(cur_value + value)
            dfs(cur_weight - weight, cur_value + value)

    dfs(max_weight, 0)
    return max(answer)



if __name__ == "__main__":
    print(packing(read_lines("./example_files/가방담기in3.txt")))
    # 1: 28, 2: 42, 3: 90

    f = open("./example_files/가방담기in1.txt", "r")
    n , limit_kg = map(int, f.readline().split())
    wbag_idx = [0] * (limit_kg + 1)
    for i in range(n):
        w, v = map(int, f.readline().split())
        for j in range(w, limit_kg + 1):
            wbag_idx[j] = max(wbag_idx[j], wbag_idx[j - w] + v)
            print(wbag_idx)
