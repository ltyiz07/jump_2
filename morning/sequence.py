from morning.file_reader import read_lines


def travel(lst):
    max_nodes = int(lst[0].split()[0])
    all_nodes = lst[0].split()[1]
    print(max_nodes, all_nodes)
    origin_node = list(map(lambda x: list(map(int, x.split())), lst[1:]))
    count = 0

    def walk(node, pos=1):
        nonlocal count
        if len(node) == 0:
            return
        if pos == max_nodes:
            count += 1
            return
        for e, n in enumerate(node):
            if pos in n:
                pos = n[int(not n.index(pos))]
                walk(node[:e] + node[e+1:], pos)
    walk(origin_node)
    return count








if __name__ == "__main__":
    print(travel(read_lines("example_files/상태변화in1.txt")))