from morning.file_reader import read_lines


def cut(read):
    need = int(read[0].split()[1])
    lines = list(map(int, read[1:-1]))
    temp_long = max(lines)
    temp_short = 1
    n = (temp_long + temp_short) // 2
    print(need)
    print(cut_count(lines, 40198))
    while cut_count(lines, n) != need:
        if cut_count(lines, n) < need:      # 개수 부족
            temp_long = n
            n = (temp_short + temp_long) // 2
        elif cut_count(lines, n) > need:      # 개수 남음
            temp_short = n
            n = (temp_short + temp_long) // 2
        print(temp_short, "    ", n, "    ", temp_long)
    while cut_count(lines, n) < need:
        n += 1
        print(n)
    print(n)
    return n



def cut_count(lst, cut_len):
    answer_lst = list(map(lambda x: x // cut_len, lst))
    answer = 0
    for ele in answer_lst:
        answer += ele
    return answer


if __name__ == "__main__":
    cut(read_lines("example_files\\랜선자르기in1.txt"))
    cut(read_lines("example_files\\랜선자르기in2.txt"))
    cut(read_lines("example_files\\랜선자르기in3.txt"))
    cut(read_lines("example_files\\랜선자르기in4.txt"))

