def solution(info, query):
    answer = []
    info_data = []
    info_data_score = []
    query_data = []
    query_data_score = []
    for i in info:
        i_list = i.split(' ')
        info_data.append(set())
        info_data_score.append(int(i_list[-1]))
        for k in i_list[:4]:
            info_data[-1].add(k)

    for q in query:
        q_list = q.split(' ')
        query_data_score.append(int(q_list[-1]))
        query_data.append({q_list[x] for x in (0, 2, 4, 6)})
        # for k in q_list[:-1]:
        #     if not ((k == '-') or (k == 'and')):
        #         query_data[-1].add(k)


    for n, q in enumerate(query_data):
        temp_num = 0
        q.discard('-')
        for m, i in enumerate(info_data):
            if query_data_score[n] <= info_data_score[m]:
                if q.issubset(i):
                    temp_num += 1
        answer.append(temp_num)

            # if q.issubset(i):
            #     pass


    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]


print(solution(info, query))