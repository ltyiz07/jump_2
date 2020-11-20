# *args 처리해 봅시다.

def lastname_and_firstname(*names):
    print(names)
    for name in names:
        print("%s %s" % (name[0], name[1:3]), end=", ")
    print('\n')


lastname_and_firstname("이선희", "이문세", "곽철용")
star_list = ["이선희", "이문세", "곽철용", "최양락", "박중용", "전경미"]

lastname_and_firstname(star_list)


def reveal(a):
    print(type(a))
    print(a)


def get_all(a, b, *x, **y):
    reveal(a)
    reveal(b)
    reveal(x)
    reveal(y)
    for key, value in y.items():
        print(f"{key}    {value}")


get_all('a', 'b', 'c', 'd', r='k', s='t')


a = "k"

dd = {a: "apple", 'b': "fight", 23: "great"}
print(dd)
print(dd['k'])