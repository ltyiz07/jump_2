from morning.file_reader import read_lines


def reading(file_name):
    r = read_lines(file_name)
    a = r[:7]
    a[0] = a[0][:-1]
    for i in range(len(a)):
        a[i] = list(map(int, a[i].split()))
    return a


def grid(lst2D, swap=False):
    import numpy as np
    count = 0
    for l in lst2D:
        for i in range(3):
            pick_five = l[i:i + 7]
            if pick_five[1] == pick_five[3] and pick_five[0] == pick_five[4]:
                count += 1
    if swap:
        return count
    else:
        return count + grid(np.transpose(lst2D), True)
    return count





if __name__ == "__main__":
    print(grid(reading("example_files\\격자판회문수1.txt")))
    print(grid(reading("example_files\\격자판회문수2.txt")))
