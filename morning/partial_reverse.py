from morning.file_reader import read_lines


def partial(origin, lst):
    lst = list(map(to_int_index, lst))
    for first, second in lst:
        origin = origin[:first] + origin[first:second][::-1] + origin[second:]
    return origin


def to_int_index(two):
    first, second = two.split(" ")
    return int(first) - 1, int(second)


if __name__ == "__main__":
    origin = [i for i in range(1, 21)]
    print(partial(origin, read_lines("./example_files/구간자리in1.txt")))