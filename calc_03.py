import feature_1.fruite


special_a = feature_1.fruite.listing("a,b,c,d,e,f")
print(special_a)


sum = None


def my_four_cal(sum, param):
    result = int(sum)
    if "+" in param:
        result = int(sum) + int(param[1:])
    elif "-" in param:
        result = int(sum) - int(param[1:])
    elif "*" in param:
        result = int(sum) * int(param[1:])
    elif "/" in param:
        result = int(sum) / int(param[1:])
    return result


while True:
    if not sum:
        sum = input("1. 입력...>")
        print("sum이 {}입니다.".format(sum))
        # break
    txt = input("입력...>")
    sum = my_four_cal(sum, txt)
    print("{}를 계산합니다.".format(txt))
    if txt == 'q':
        break