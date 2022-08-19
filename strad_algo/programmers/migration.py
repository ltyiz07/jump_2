def get_n_fit(duration, times):
    total_flow = 0
    for time in times:
        total_flow += duration // time
    return total_flow
        

def solution(n, times):
    min_t = 1
    max_t = min(times) * n
    cur_p = 0
    while min_t != max_t:
        mean_t = (min_t + max_t) // 2
        cur_p = get_n_fit(mean_t, times)
        if cur_p >= n:
            max_t = mean_t
        else:
            min_t = mean_t + 1
    return max_t



if __name__ == "__main__":
    print(solution(6, [7, 10]))

