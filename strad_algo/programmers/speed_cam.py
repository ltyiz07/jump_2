def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam_pos = -30001
    for (start, end) in routes:
        if cam_pos < start:
            cam_pos = end
            answer += 1
    return answer


if __name__ == "__main__":
    my_answer = solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
    print(f"{my_answer} should be 2")
