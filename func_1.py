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




if __name__ == "__main__":mmat
    s = "1,3,4,22,2"
    i = 2

    r = chk_dupl(s, i)
    print(r)

    def fn():
        print("#######")

    class MyClass:
        def __init__(self):
            print("$$$$$$$$$$$$$$$$$$$$$$$$")

    a = fn()

    b = MyClass
    b()

    c = MyClass()
    # c()           # TypeError: "MyClass" object is not callable