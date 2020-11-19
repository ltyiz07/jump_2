my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]



class MyError(Exception):
    pass

curse = "fuck", "damn", "bitch", "shit"
i = 0
b = ""
while i == 0:
    a = input("put id: ")
    try:
        if curse.count(a) != 0:
            raise MyError()
        else:
            print("it it right ? : %s  [Y, N]" % a)
            b = input()
    except MyError:
        print("use another ID")
    finally:
        if b == 'Y':
            i += 1
            name = a
print(name)