def repeat_n(number, repeat):
    assert 0 < number and number < 10
    assert 0 < repeat
    value = number
    while repeat != 1:
        repeat -= 1
        value += (10 ** repeat) * number
    return value


def solution(N, number):
    """
    possible operations: repeat, plus, minus, times, divide
    """
    answer = 1
    pool = {N}
    pools = [pool]
    while number not in pool:
        if answer > 7:
            return -1
        pool = {repeat_n(N, answer + 1)}
        for left in range(1, (answer + 1) // 2 + 1):
            right = (answer + 1) - left
            for x_ in pools[left-1]:
                for y_ in pools[right-1]:
                    pool.add(x_ + y_)
                    pool.add(x_ * y_)
                    pool.add(x_ - y_)
                    pool.add(y_ - x_)
                    if y_ != 0:
                        pool.add(x_ // y_)
                    if x_ != 0:
                        pool.add(y_ // x_)
        pools.append(pool)
        answer += 1
    return answer


if __name__ == "__main__":
    print(solution(8, 53))
