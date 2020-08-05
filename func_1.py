s = "1,3,4,22,2"
i = 2                       #taget is integer

      #string to integer convert


def find_num(list_1, pi):
    temp = False
    for i in list_1:
        if int(i) == pi:
            temp = True
    return temp


def chk_dupl(ps, pi):
    temp = False
    list_s = ps.split(',')
    if find_num(list_s, pi):
        temp = True
    return temp


r = chk_dupl(s, i)

if __name__ == "__main__":

    print(chk_dupl(s, i))


    a = 1

    def fn():
        print("#######")

    class MyClass:
        print("$$$$$$$$$$$$$$$$$$$$$$$$")


    if __name__ == "__main__":
        print("hello world.")
