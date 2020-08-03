def solution(prices):
    index = 0
    answer = []
    for i in prices:
        count = 0
        for j in prices[index + 1:]:
            count += 1
            if i > j: break
        answer.append(count)
        index += 1
    return answer

print(solution([1, 2, 3, 2, 3]))