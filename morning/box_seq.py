def box(from_file):
    b = from_file[0]
    s = from_file[1]
    for _ in range(s):
        b[b.index(max(b))] -= 1
        b[b.index(min(b))] += 1
    return max(b) - min(b)


def file_read(file_name):
    with open(file_name, 'r') as f:
        f.readline()
        out_lst = list(map(int, f.readline().split()))
        s = int(f.readline())
    return out_lst, s


if __name__ == "__main__":
    print(file_read(".\\example_files\\창고정리1.txt"))
    print(file_read(".\\example_files\\창고정리2.txt"))
    print(box(file_read(".\\example_files\\창고정리1.txt")))
    print(box(file_read(".\\example_files\\창고정리2.txt")))

