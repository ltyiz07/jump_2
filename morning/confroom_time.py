def get_times(file_name):
    answer = []
    with open(file_name, 'r') as f:
        n = int(f.readline())
        for i in range(n):
            answer.append(tuple(map(int, f.readline().split())))
    answer = end_sort(answer)
    temp_front, temp_back = 0, 0
    count = 0
    for i in answer:
        if i[1] == 0:
            temp_back = i[1]
            continue
        elif temp_back <= i[0]:
            count += 1
            temp_back = i[1]
    return count


def end_sort(lst):
    end_sorted = sorted(lst, key=lambda end: (end[1], -end[0]))
    return end_sorted


if __name__ == "__main__":
    print(get_times("example_files/회의실in1.txt"))
    print(get_times("example_files/회의실in2.txt"))
