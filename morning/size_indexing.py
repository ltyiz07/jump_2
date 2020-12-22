from morning.file_reader import read_lines
import numpy as np


# def reversing(lst):
#     length = int(lst[0])
#     line = np.array(list(map(int, lst[1].split())))
#     max_value = line.max()
#     answer = []
#     print(line)
#     for _ in range(length):
#         temp_index = line.argmin()
#         answer.append(temp_index + 1)
#         line[temp_index] = max_value + 1
#
#     return answer
# 4 8 9 6 1 3 10 7 5 2

def reversing(lst):
    length = int(lst[0])
    line = list(map(int, lst[1].split()))
    maximum = length + 1
    answer = [length + 1] * length
    print(answer)
    print(line)
    for i, e in enumerate(line):
        idx = i + 1
        pos = e
        for l in answer:
            if l < idx:
                pos -= 1
            elif pos == -1:
                pass


if __name__ == "__main__":
    print(reversing(read_lines("example_files/역수열in1.txt")))
