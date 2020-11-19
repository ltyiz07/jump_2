import time
wave = "===="
latch = 0
while True:
    if len(wave) == 100:
        latch = 1
    elif len(wave) == 4:
        latch = 0

    if latch == 0:
        wave += '$'
    elif latch == 1:
        wave = wave[:len(wave)-1]
    print(wave)
    time.sleep(0.01)

