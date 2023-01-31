def subtract_month(date, n_month):
    """
    get new date before n_month from input date
    """
    date = [int(n) for n in date.split(".")]
    m = int(n_month)
    if m > 12:
        date[0] -= m // 12
        m = m % 12
    if date[1] > m:
        date[1] -= m
    else:
        date[1] += (12 - m)
        date[0] -= 1
    return f"{date[0]}.{date[1]:0>2}.{date[2]:0>2}"

def solution(today, terms, privacies):
    answer = []
    date_last = {x[0]: subtract_month(today, x.split(" ")[1]) for x in terms}
    is_prev_fresh = {x[0]: False for x in terms}
    for e, privacy in enumerate(privacies):
        c_date, c_term = privacy.split(" ")
        if is_prev_fresh[c_term] or date_last[c_term] >= c_date:
            answer.append(e + 1)
        else:
            is_prev_fresh[c_date] = True
    return answer


if __name__ == "__main__":
    assert solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]) == [1, 3]
    assert solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]) == [1, 4, 5]
