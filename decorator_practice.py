def deco(func):
    def new_func(a, b):
        print(a, b)
        return func(a, b)
    return new_func

def adder(a, b):
    return a + b

deco(adder)

def prac():
    def praca(a, b):
        print(a, b)
    return praca
