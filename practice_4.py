import math
import time


def wave(n):
    for i in range(n):
        print('$' * n)

degree = 0
while True:
    degree += 4
    if degree == 361:
        degree = 0
    ran = int(math.sin(math.radians(degree)) * 200)
    wave(ran)
    time.sleep(0.1)
