""""## 기출 문제

### orders
#### ["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]

#### result ["bob"]

#### ["alex pizza pasta steak", "bob noodle sandwich pasta", "choi pizza sandwich pizza", "alex pizza pasta steak"]

#### result ["alex", "bob"]

#### 입출력 예 설명
- "alex"와 "bob"은 음식 세 종류를 주문했으며, "choi"는 두 종류를 주문했습니다. 따라서 오름차순 정렬하여 ["alex", "bob"] 을 return 하면 됩니다.
"""
def order(lst=[]):
    orders = dict()
    for l in lst:
        temp = l.split()
        for i in temp[1:]:
            if temp[0] in orders:
                orders[temp[0]].add(i)
            else:
                orders[temp[0]] = {i}
    temp = 0
    answer = []
    for p, o in orders.items():
        if temp < len(o):
            temp = len(o)
            answer = [p]
        elif temp == len(o):
            answer.append(p)
    return sorted(answer)


if __name__ == "__main__":
    print(order(["alex pizza pasta", "alex pizza  pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]))
    print(order(["alex pizza pasta steak", "bob noodle sandwich pasta", "choi pizza sandwich pizza", "alex pizza pasta steak"]))