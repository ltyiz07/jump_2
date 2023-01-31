
def cutter(n, stack = 0):
    if n == 1:
        return stack

    stack += 1
    return cutter( (n + 1) // 2, stack )


def solution(arr, stack=0):
    if len(arr) == 1:
        return arr
    arr = arr[::-1]
    half_point = (len(arr) + 1) // 2
    return solution(arr[:half_point]) + solution(arr[half_point:])


if __name__ == "__main__":
    for i in range(2, 30):
        a = solution(list(range(i)))
        print(f"{i:2}: {a.index(0):2} {a.index(1):2} {a}\t")
