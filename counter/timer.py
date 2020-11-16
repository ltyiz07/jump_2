import timeit


class Timer:
    def __init__(self):
        self.start_time = 0
        self.finish_time = 0

    def start(self):
        self.start_time = timeit.default_timer()

    def finish(self):
        self.finish_time = timeit.default_timer()
        print("%f micro sec 걸렸습니다." % ((self.finish_time - self.start_time) * 1000000))
