def digit_sum(file_name):
    with open(file_name, 'r') as f:
        f.readline()
        lst = f.readline().split(' ')
    added = []
    for each in lst:
        temp_int = 0
        for c in each:
            temp_int += int(c)
        added.append(temp_int)
    big = max(added)
    answer = []
    print(big)
    print(added)
    print(lst)
    for e, i in enumerate(added):
        if big == i:
            answer.append(lst[e])
    return answer



print(digit_sum("자릿수합input1.txt"))
print(digit_sum("자릿수합input2.txt"))
