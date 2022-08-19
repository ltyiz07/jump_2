def solution(people, limit):
    answer = 0
    matched = 0
    people.sort()
    last_matched = len(people) - 1
    for light_idx in range(0, len(people) - 1):
        for heavy_idx in range(last_matched, light_idx, -1):
            if (people[light_idx] + people[heavy_idx]) <= limit:
                matched += 1
                last_matched = heavy_idx - 1
                break
    answer = len(people) - matched
    return answer


if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))
