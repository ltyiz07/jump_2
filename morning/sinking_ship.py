from morning.file_reader import read_lines
from collections import deque


def sinking_ship(lst=[]):
    m = int(lst[0].split()[1])
    second_line = deque(sorted(list(map(int, lst[1].split()))))

    count = 0
    while len(second_line) > 1:
        if second_line[0] + second_line[-1] > m:
            second_line.pop()
            count += 1
        else:
            second_line.pop(0)
            second_line.pop()
            count += 1
            
    return count


if __name__ == "__main__":
    print(sinking_ship(read_lines("example_files\\침몰타이타닉1.txt")))
    print(sinking_ship(read_lines("example_files\\침몰타이타닉2.txt")))
    print(sinking_ship(read_lines("example_files\\침몰타이타닉4.txt")))
