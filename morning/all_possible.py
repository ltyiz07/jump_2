def bin_to_list_all(n):
    answer = []
    for i in range(2 ** n):
        answer.append(bin_to_list(i, n))
    return answer


def bin_to_list(b, n):
    bin_string = bin(b)
    bin_string = bin_string[2:]
    bin_string = list(map(int, list(bin_string)))
    while len(bin_string) != n:
        bin_string.insert(0, 0)
    return bin_string


def all_kind(lst):
    """
    make bincary checker and compare.
    :param lst: Iterable
    :return: list[][]
    """
    n = len(lst)
    answer = []
    for i in bin_to_list_all(n):
        temp = []
        for l in range(n):
            if i[l] == 1:
                temp.append(lst[l])
        answer.append(temp)
    return answer


if __name__ == "__main__":
    print(all_kind([1, 2, 3, 4, 5]))