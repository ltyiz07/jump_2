# 제네레이터

a = [1, 2, 3, 4, 5]
it = iter(a)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# 이 이상으로 사용하면 StopIteration 오류발생


print("=" * 50)
# 함수 내부에 yield를 사용하면 제네레이터 함수가 된다.

def my_gen():
    n = 0
    while n <= 10:
        yield n
        n += 1


b = my_gen()
type(b)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
