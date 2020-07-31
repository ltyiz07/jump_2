# 테스트 1 〉	통과 (0.05ms, 10.6MB)
# 테스트 2 〉	통과 (0.06ms, 10.9MB)
# 테스트 3 〉	통과 (0.06ms, 10.6MB)
# 테스트 4 〉	통과 (1.29ms, 10.8MB)
# 테스트 5 〉	통과 (0.06ms, 10.8MB)
# 테스트 6 〉	통과 (0.06ms, 10.8MB)
# 테스트 7 〉	통과 (0.13ms, 10.8MB)
# 테스트 8 〉	통과 (0.38ms, 10.8MB)
# 테스트 9 〉	통과 (0.33ms, 10.8MB)
# 테스트 10 〉	통과 (0.38ms, 10.8MB)
# 테스트 11 〉	통과 (0.77ms, 10.8MB)

data = """테스트 1 〉	통과 (0.05ms, 10.6MB)
테스트 2 〉	통과 (0.06ms, 10.9MB)
테스트 3 〉	통과 (0.06ms, 10.6MB)
테스트 4 〉	통과 (1.29ms, 10.8MB)
테스트 5 〉	통과 (0.06ms, 10.8MB)
테스트 6 〉	통과 (0.06ms, 10.8MB)
테스트 7 〉	통과 (0.13ms, 10.8MB)
테스트 8 〉	통과 (0.38ms, 10.8MB)
테스트 9 〉	통과 (0.33ms, 10.8MB)
테스트 10 〉	통과 (0.38ms, 10.8MB)
테스트 11 〉	통과 (0.77ms, 10.8MB)"""

def ms_calc(data):
    str_time = ""
    count = 0
    ms_count = 0
    time = 0
    for i in data:
        if data[count] == 'm':
            if data[count + 1] == 's':
                print(data[count - 4:count])
                time += float(data[count - 4:count])
        count += 1
    print(time / count)
    return time / count
