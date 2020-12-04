from morning.file_reader import read_lines, print_2d


def block_count(lst):
    size = int(lst[0])
    print(size)
    town = []
    for l in lst[1:-1]:
        town.append(list(map(int, l.split())))
    print_2d(town)

    def counter(pos):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):



if __name__ == "__main__":

    block_count(read_lines("example_files/town1.txt"))