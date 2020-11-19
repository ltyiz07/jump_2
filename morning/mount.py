def get_data(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        region = []
        for _ in range(n):
            region.append(f.readline().split())
        region = [list(map(int, l)) for l in region]
    return n, region


def mount(data):
    n = data[0]
    region = data[1]
    count = 0

    # 위아래 같은 크기의 0들 1행 추가.
    region.insert(0, [0 for _ in range(n)])
    region.append([0 for _ in range(n)])

    # 왼쪽, 오른쪽에 0들 한씩열 추가
    for e in range(n + 2):
        region[e].insert(0, 0)
        region[e].append(0)

    for i, lst in enumerate(region):
        for e, el in enumerate(lst):
            if el != 0:
                if (region[i - 1][e] < el) and (region[i + 1][e] < el) and
                        (region[i][e + 1] < el) and (region[i][e - 1] < el):
                    count += 1

    return count


print(mount(get_data("봉우리in1.txt")))
print(mount(get_data("봉우리in2.txt")))