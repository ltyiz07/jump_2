import winsound
from random import random
import matplotlib.pyplot as plt


def average(lst):
    length = len(lst)
    temp = 0
    for i in lst:
        temp += i
    return round(temp / length, 4)


def one_shot(n):
    target = set()
    for _ in range(n):
        r = int(random() * n) + 1
        target.add(r)
    return len(target)


def all_shot(n):
    target = set()
    count = 1
    while len(target) != n:
        r = int(random() * n) + 1
        target.add(r)
        count += 1
    return count


def mount_graph(graph_target):
    x_ = range(min(graph_target), max(graph_target) + 1)
    y_ = []
    for val in x_:
        y_.append(graph_target.count(val))
    plt.plot(x_, y_)
    plt.show()


if __name__ == "__main__":
    winsound.Beep(280, 300)
    winsound.Beep(200, 300)
    hit_lst = []
    for hit in range(10000):
        hit_lst.append(one_shot(10000))
    print(hit_lst)
    mount_graph(hit_lst)
    winsound.Beep(280, 300)


    # shot_lst = []
    # for hit in range(10000):
    #     shot_lst.append(all_shot(10))
    # print(average(shot_lst))
    winsound.Beep(200, 300)
    winsound.Beep(280, 300)
