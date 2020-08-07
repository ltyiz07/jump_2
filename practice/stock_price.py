def solution(prices):
    k = len(prices) - 1
    for i, aprice in enumerate(prices):
        for j in range(k):            # 리스트 슬라이싱 대신 인덱싱 '-n'사용하여 해결.
            if aprice > prices[j - k]:
                break
        prices[i] = j + 1
        k -= 1
    prices[-1] = 0

    return prices

print('sol', solution([1, 2, 3, 4, 2, 1]))
print('ans', [5, 4, 2, 1, 1, 0])
print(solution([1, 2, 3, 2, 3]))
print([4, 3, 1, 1, 0])
print(solution([6,7,6,8,6,7,8,9,10,9,10,9,8,6,6,5,4,3,4,5]))