import winsound
from random import random
import matplotlib.pyplot as plt


def average(lst):
    """
    리스트의 모든 값들을 더해서 평균을 구해줌.
    :param lst: int[]
    :return: int(average)
    """
    length = len(lst)
    temp = 0
    for i in lst:
        temp += i
    return round(temp / length, 4)


def one_shot(n):
    """
    1부터 n 까지(n개의 수) 랜덤하게 하나의 수를 n번 뽑았을때
    겹치지 않는 수들의 갯수.
    :param n:
    :return:
    """
    target = set()
    for _ in range(n):
        r = int(random() * n) + 1
        target.add(r)
    return len(target)


def all_shot(n):
    """
    1 부터 n 까지의 중 랜덤하게 하나의 수를 뽑았을때
    겹치지 않게 추가되는 수가 n 개가 되는 횟수.
    :param n:
    :return:
    """
    target = set()
    count = 1
    while len(target) != n:
        r = int(random() * n) + 1
        target.add(r)
        count += 1
    return count


def mount_graph(graph_target):
    winsound.Beep(280, 300)
    """
    리스트에서 각각의 수들의 갯수를 그래프로 그려줌.
    :param graph_target:
    :return:
    """
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


    # shot_lst = []
    # for hit in range(10000):
    #     shot_lst.append(all_shot(10))
    # print(average(shot_lst))
    winsound.Beep(200, 300)
    winsound.Beep(280, 300)
