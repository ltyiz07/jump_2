def get_times(file_name):
    answer = []
    with open(file_name, 'r') as f:
        n = f.readline()
        for i in range(n):
            list(map(int, f.readline().split()))

def end_sort(lst):
    end_sorted = sorted(lst, key=lambda end: end[1])
    return end_sorted
