



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


data_1 = """통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.07ms, 10.1MB)
테스트 3 〉	통과 (1.12ms, 10.3MB)
테스트 4 〉	통과 (1.24ms, 10.3MB)
테스트 5 〉	통과 (1.48ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.71ms, 10.3MB)
테스트 8 〉	통과 (0.83ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (1.44ms, 10.3MB)"""
ms_calc(data_1)


