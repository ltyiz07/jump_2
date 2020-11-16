def fact(input_num):
    if input_num == 1:
        return 1
    return input_num * fact(input_num - 1)

print(fact(2))