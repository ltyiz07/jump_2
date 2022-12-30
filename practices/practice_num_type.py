
move_costs = {
    (0, 0): 1, (0, 1): 7, (0, 2): 6, (0, 3): 7, (0, 4): 5, (0, 5): 4, (0, 6): 5, (0, 7): 3, (0, 8): 2, (0, 9): 3,
    (1, 1): 1, (1, 2): 2, (1, 3): 4, (1, 4): 2, (1, 5): 3, (1, 6): 5, (1, 7): 4, (1, 8): 5, (1, 9): 6,
    (2, 2): 1, (2, 3): 2, (2, 4): 3, (2, 5): 2, (2, 6): 3, (2, 7): 5, (2, 8): 4, (2, 9): 5,
    (3, 3): 1, (3, 4): 5, (3, 5): 3, (3, 6): 2, (3, 7): 6, (3, 8): 5, (3, 9): 4,
    (4, 4): 1, (4, 5): 2, (4, 6): 4, (4, 7): 2, (4, 8): 3, (4, 9): 5,
    (5, 5): 1, (5, 6): 2, (5, 7): 3, (5, 8): 2, (5, 9): 3,
    (6, 6): 1, (6, 7): 5, (6, 8): 3, (6, 9): 2,
    (7, 7): 1, (7, 8): 2, (7, 9): 4,
    (8, 8): 1, (8, 9): 2,
    (9, 9): 1,
}


def get_cost(f, t):
    arr = (int(f), int(t))
    return move_costs[(min(arr), max(arr))]


def solution(numbers):

    # Key: 0 is left 1 is right
    # Value: (key1, key2, cost)
    table = {("6", "4"): 0}

    for n in numbers:
        table_copy = table.copy()
        table = dict()
        for (key2, key1), cost in table_copy.items():
            if (key2 == n) or (key1 == n):
                k = (key2, key1)
                if k in table:
                    table[k] = table[k] if table[k] <= cost + 1 else cost + 1
                else:
                    table[k] = cost + 1
            else:
                added_cost = get_cost(key2, n)
                k = (n, key1) if n > key1 else (key1, n)
                if k in table:
                    table[k] = table[k] if table[k] <= cost + added_cost else cost + added_cost
                else:
                    table[k] = cost + added_cost

                added_cost = get_cost(key1, n)
                k = (key2, n) if key2 > n else (n, key2)
                if k in table:
                    table[k] = table[k] if table[k] <= cost + added_cost else cost + added_cost
                else:
                    table[k] = cost + added_cost

        # pprint(table)
        # print()

    return min(table.values())


def solution_1(numbers):

    # Key: 0 is left 1 is right
    # Value: (left, right, cost)
    table = {"": ("4", "6", 0)}

    for n in numbers:
        table_copy = table.copy()
        table = dict()
        for k, v in table_copy.items():
            (left, right, cost) = v
            if n == left:
                table[k + "0"] = (left, right, cost + 1)
            elif n == right:
                table[k + "1"] = (left, right, cost + 1)
            else:
                added_cost = get_cost(left, n)
                table[k + "0"] = (n, right, cost + added_cost)
                added_cost = get_cost(right, n)
                table[k + "1"] = (left, n, cost + added_cost)
        # pprint(table)
        # print()
    return min(table.values(), key=lambda x: x[2])[2]


def pprint(target):
    for k, v in target.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    # sol = solution("1756")    # result: 10
    test_input = "251529"
    sol = solution(test_input)
    sol_1 = solution_1(test_input)
    print(f"{sol}, {sol_1}, {sol == sol_1}")
