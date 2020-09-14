import timeit

def timer(func):
    def new_func(*a, **b):
        start = timeit.default_timer()
        func(*a, **b)
        finish = timeit.default_timer()
        print(finish - start)
        return func(*a, **b)
    return new_func

if __name__ == '__main__':
    @timer
    def adder(a, b):
        for i in range(100000):
            pass
        return a + b


    print(adder(2, 5))
