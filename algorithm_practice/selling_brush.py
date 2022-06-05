
def solution(enroll, referral, seller, amount):
    brush_price = 100
    share_ratio = 10
    profits = [0] * len(enroll)

    # enroll_table = {name: index for index, name in enumerate(enroll)}
    # share_trees = {name: get_upper2(enroll_table, referral, enroll_table.get(name)) for name in enroll}
    share_trees = get_upper3(enroll, referral)

    for who, sell_count in zip(seller, amount):
        earn = sell_count * brush_price
        if earn < 10:
            profits[share_trees.get(who).pop()] += earn
            continue
        for share_holder_index in share_trees.get(who):
            if earn < 10:
                profits[share_holder_index] += earn
                break
            profit = earn - earn // share_ratio
            profits[share_holder_index] += profit
            earn -= profit

    return profits


def get_upper(ordered_names: list, bringer: list, index: int) -> list:
    if bringer[index] == "-":
        return [index]
    else:
        ordered_name_index = ordered_names.index(bringer[index])
        return [index] + get_upper(ordered_names, bringer, ordered_name_index)


def get_upper2(ordered_names: dict, bringer: list, index: int) -> list:
    answer = [index]
    share_holder = bringer[index]
    while share_holder != "-":
        share_holder_index = ordered_names.get(share_holder)
        answer.append(share_holder_index)
        share_holder = bringer[share_holder_index]
    return answer


def get_upper3(ordered_names: dict, bringer: list) -> dict:
    tree_table = dict()
    for index, name in enumerate(ordered_names):
        if bringer[index] == "-":
            tree_table[name] = [index]
        else:
            tree_table[name] = [index] + tree_table.get(bringer[index])
    return tree_table


def get_upper_count(ordered_names: list, bringer: list, index: int) -> int:
    if bringer[index] == "-":
        return 1
    else:
        ordered_name_index = ordered_names.index(bringer[index])
        return 1 + get_upper_count(ordered_names, bringer, ordered_name_index)


if __name__ == "__main__":
    t_enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    t_referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    # dynamic table 방식으로 트리 생성하기
    # 모든 자손들은 "-" 으로 수렴하는 "john"과 "mary" 의 자손들다.
    # t_seller = ["young", "john", "tod", "emily", "mary"]
    # t_amount = [12, 4, 2, 5, 10]
    t_seller = ["young", "john", "tod", "emily", "mary", "young", "mary", "young", "sam"]
    t_amount = [10, 4, 2, 5, 5, 2, 5, 0, 0]

    t_result = [360, 958, 108, 0, 450, 18, 180, 1080]

    print()
    print(solution(t_enroll, t_referral, t_seller, t_amount) == t_result)
    print("**** result: ", t_result)
    print("**** answer: ", solution(t_enroll, t_referral, t_seller, t_amount))

    print(get_upper(t_enroll, t_referral, 0))
