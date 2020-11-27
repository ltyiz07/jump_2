from morning.file_reader import read_lines
from collections import deque


def order(lst):
    lst[0] = tuple(map(int, lst[0].split()))
    h = lst[0][1]
    print(lst[0])
    patient_lst = list(map(int, lst[1].split()))
    del lst
    print(patient_lst)
    count = 0
    while True:
        large_index = patient_lst.index(max(patient_lst))
        if large_index > h:
            patient_lst.pop(large_index)
            count += 1
            continue
        elif large_index < h:
            patient_lst.pop(large_index)
            count += 1
            h -= 1
            continue
        elif large_index == h:
            return count + 1


def order_deque(lst):
    lst[0] = tuple(map(int, lst[0].split()))
    n, m = lst[0]
    patient_lst = deque(map(int, lst[1].split()))
    del lst

    enum_lst = [(idx, int(xx)) for idx, xx in enumerate(patient_lst)]
    Q = deque(enum_lst)
    cnt = 0
    while True:
        now = Q.popleft()
        if any(now[1] < x[1] for x in Q):
            Q.append(now)
        else:
            cnt += 1
            if now[0] == m:
                break
    print(f"지정하신 {m} 환자의 진료 차례는 {cnt}번째 입니다.")


if __name__ == "__main__":
    order_deque(read_lines("example_files\\응급실in1.txt"))
    print(order_deque(read_lines("example_files\\응급실in2.txt")))
    order_deque(read_lines("example_files\\응급실in2.txt"))

