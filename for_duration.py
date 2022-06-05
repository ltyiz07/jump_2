import time

def pure_for(n=100000):
    start = time.perf_counter()

    a = 0
    for i in range(n):
        a = i

    print(f"pure_for duration: {time.perf_counter() - start}")

def comp_for(n=100000):
    start = time.perf_counter()

    a = 0
    [i for i in range(n)]
    
    print(f"comp_for duration: {time.perf_counter() - start}")



if __name__ == "__main__":
    pure_for()
    comp_for()
