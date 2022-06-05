def shift_left(ar: list, k: int):
    if k < 1 or k > len(ar) - 1:
        return
    x = ar.pop()
    ar.insert(0, x)
    shift_left(ar, k - 1)


if __name__ == "__main__":
    ll = [1, 2, 3, 4, 5, 6, 7]
    shift_left(ll, 4)
    print(ll)
