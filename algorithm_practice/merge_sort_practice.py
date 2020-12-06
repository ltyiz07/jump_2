def merge_sort(lst=[]):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] <= lst[1]:
            a = [lst[0], lst[1]]
            return a
        else:
            a = [lst[1], lst[0]]
            return a
    else:
        a = merge_sort(lst[:len(lst) // 2 + 1])
        b = merge_sort(lst[len(lst) // 2 + 1:])
        temp = []
        while a or b:
            if not a:
                temp.append(b.pop(0))
            elif not b:
                temp.append(a.pop(0))
            elif a[0] <= b[0]:
                temp.append(a.pop(0))
            else:
                temp.append(b.pop(0))
        return temp


def pick_sort(lst):
    enum = [i for i in range(len(lst))]
    for i, l in zip(enum, lst):
        temp_index = i
        for j, m in zip(enum[i+1:], lst[i+1:]):
            if lst[temp_index] > m:
                temp_index = j
        lst[i], lst[temp_index] = lst[temp_index], lst[i]

    return lst




if __name__ == "__main__":
    import random
    rand_lst = []

    for i in range(100):
        rand_lst.append(int(random.random() * 10000) + 1)

    from timeit import default_timer as timer
    start_time1 = timer()
    merge_sort(rand_lst)
    merge_sort(rand_lst)
    merge_sort(rand_lst)
    merge_sort(rand_lst)
    merge_sort(rand_lst)
    end_time1 = timer()
    print(end_time1 - start_time1)

    start_time2 = timer()
    pick_sort(rand_lst)
    pick_sort(rand_lst)
    pick_sort(rand_lst)
    pick_sort(rand_lst)
    pick_sort(rand_lst)
    end_time2 = timer()
    print(end_time2 - start_time2)
