def make_list(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline())
        farm = [list(map(int, file.readline().split())) for _ in range(n)]
        return n, farm


def apple_tree(farm_land):
    print('*' * 50)
    n = farm_land[0]
    farm = farm_land[1]
    add_up = []
    for i in range(n):
        if i <= (n / 2):
            add_up.append(farm[i][n//2 - i:n//2 + i + 1])
        else:
            add_up.append(farm[i][n // 2 - (n - i - 1):n // 2 + (n - i)])
    answer = 0
    for k in add_up:
        print(k)
        for j in k:
            answer += j
    print('*' * 50)
    return answer

def  gen_n_matrix(n):
    import random
    random.seed(0)
    with open(f"{str(n)}_matrix.txt", "w") as f:
        f.write(str(n))
        f.write(str([[random.randint(1, n * n) for i in range(n)] for j in range(n)]))


    return [[random.randint(1, n * n) for i in range(n)] for j in range(n)]

if __name__ == "__main__":
    print(apple_tree(make_list("example_files/apple_tree_1.txt")))
    print(apple_tree(make_list("example_files/apple_tree_2.txt")))

    for i in gen_n_matrix(3):
        print(i)
