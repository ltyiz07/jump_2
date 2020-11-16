



def ms_calc(data):
    count = 0
    time = 0
    for i in range(len(data)):
        if data[count] == 'm':
            if data[count + 1] == 's':
                time += float(data[count - 4:count])
        count += 1
    print(time / count)
    return time / count


data_1 = """테스트 1 〉	통과 (0.17ms, 9.81MB)
테스트 2 〉	통과 (0.18ms, 9.73MB)
테스트 3 〉	통과 (0.86ms, 9.83MB)
테스트 4 〉	통과 (5.44ms, 10.2MB)
테스트 5 〉	통과 (20.32ms, 10.3MB)
테스트 6 〉	통과 (31.70ms, 10.2MB)
테스트 7 〉	통과 (16.62ms, 10.8MB)
테스트 8 〉	통과 (68.50ms, 12.9MB)
테스트 9 〉	통과 (69.05ms, 13MB)
테스트 10 〉	통과 (69.70ms, 13.1MB)
테스트 11 〉	통과 (14.40ms, 10.2MB)
테스트 12 〉	통과 (42.65ms, 10.3MB)
테스트 13 〉	통과 (15.09ms, 10.9MB)
테스트 14 〉	통과 (62.85ms, 11.4MB)
테스트 15 〉	통과 (62.24ms, 11.4MB)
테스트 16 〉	통과 (14.08ms, 10.3MB)
테스트 17 〉	통과 (29.46ms, 10.2MB)
테스트 18 〉	통과 (63.83ms, 11.4MB)"""
ms_calc(data_1)


