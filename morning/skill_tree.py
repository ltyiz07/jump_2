from morning.file_reader import read_lines
from collections import deque


def skill_order(lst):
    order, length, tree = reset(lst)
    print(order, length, tree)
    answer = []
    for t in tree:
        temp_order = order.copy()
        for l in t:
            if l in temp_order:
                if l != temp_order.popleft():
                    answer.append("No")
                    break
        else:
            if not temp_order:
                answer.append("Yes")
            else:
                answer.append("No")
    return answer


def reset(lst):
    order = deque(lst[0])
    length = lst[1]
    tree = []
    for i in lst[2:-1]:
        tree.append(deque(i))
    return order, length, tree



if __name__ == "__main__":
    print(skill_order(read_lines("example_files/전공필수in2.txt")))
