def perm(lst):
    if len(lst) == 2:
        return lst, list(reversed(lst))
    


if __name__ == "__main__":
    perm([1, 2, 3, 4])