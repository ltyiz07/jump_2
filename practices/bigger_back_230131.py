from heapq import heappush, heappop

def solution(numbers):
    answer = [-1] * len(numbers)
    h = []
    for e, val in enumerate(numbers):
        while h and h[0][0] < val:
            _, i = heappop(h)
            answer[i] = val
        heappush(h, [val, e])
    return answer

if __name__ == "__main__":
    # assert solution([2, 3, 3, 5]) == [3, 5, 5, -1]
    # assert solution([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1]
    # assert solution([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    # assert solution([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]
    assert solution([3, 2, 1, 2, 3]) == [-1, 3, 2, 3, -1]
