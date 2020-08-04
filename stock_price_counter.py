def solution(prices):
    index = 0
    for i in prices:
        count = 0
        for j in prices[index + 1:]:
            count += 1
            if i > j:
                break
        prices[index] = count
        # answer.append(count)          # 대신해서 미리 리스트 만들고 지정만해주기
        index += 1
    return prices

# 효율성 문제 해결하기...

print(solution([1, 2, 3, 2, 3]))
print(solution([4, 5, 6, 7, 7, 6, 5, 4, 5, 5, 6, 5, 7]))
print([12, 6, 4, 2, 1, 1, 1, 5, 4, 3, 1, 1, 0])
