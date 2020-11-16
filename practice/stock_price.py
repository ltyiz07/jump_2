def solution(prices):
    j = 0
    k = len(prices) - 1
    for i, aprice in enumerate(prices):
        for j in range(k):            # 리스트 슬라이싱 대신 인덱싱 '-n'사용하여 해결.
            if aprice > prices[j - k]:
                break
        prices[i] = j + 1
        k -= 1
    prices[-1] = 0

    return prices
