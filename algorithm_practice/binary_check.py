from algorithm_practice.pick_n_index import gen


def binary_check(lst, bin_check=None):
    if not bin_check:
        bin_check = [[0 for _ in l] for l in lst]
        for e, l in enumerate(bin_check):
            bin_check[e][-1] = 1
    print(bin_check)
    print(bin_check[0].index(1))



if __name__ == "__main__":

    gen_lst = gen(3, 2), gen(4, 4), gen(4, 2)
    print(gen_lst)

    binary_check(gen_lst)
