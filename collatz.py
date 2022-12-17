nums = dict()

def append_num(x):
    global nums
    nums[x] = nums.get(x, 0) + 1

pre = {16: 3, 5:5}

def solution(num):
    global nums
    if num == 0:
        return -1
    elif num == 1:
        return 0
    for i in range(500):
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        append_num(num)
        if num == 1:
            return i + 1
    return -1


if __name__ == "__main__":
    for i in range(500):
        solution(i)
    print(solution(16))
