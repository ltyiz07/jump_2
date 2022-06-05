import sys
from functools import cache

from counter.timer import Timer


def loop_1(n):
    output = 0
    for i in range(n + 1):
        output += i
    return output
        
sys.setrecursionlimit(1500)
def recurse_1(n):
    if n == 0:
        return 0
    return n + recurse_1(n-1)


def loop_2(n):
    pass

def recurse_2(n):
    pass

if __name__ == "__main__":
    timer = Timer()

    assert loop_1(100) == recurse_1(100)

    timer.start()
    print(loop_1(100))
    timer.finish()
    timer.start()
    print(recurse_1(100))
    timer.finish()
