# 1부터 100 까지 랜덤으로 하나의 수를 뽑았을때 100번의 연산만에 채워질 확률. {9.33262154439438e-43}
a = 1
for i in range(100):
    a = a * (1 - (0.01 * i))

print(a)


# 1부터 10 까지 랜덤으로 하나의 수를 뽑았을때 10번의 연산만에 채워질 확률. {0.6281565095552945}
b = 1
for i in range(10):
    b = b * (1 - (0.01 * i))


#그러다면 n 개의 수를 채우는데 n번의 랜덤 기회만 준다면... 몇개의 수가 채워질까
c = 0
for i in range(1000):
    c = c + 1 - (1 / 1000 * i)

print(round(c, 4))
print(b)
# 1 부터 10 까지 랜덤으로 하나의 수를 뽑았을때 모든수를 뽑게되는데까지 필요한 평균적인 횟수... 일단 최소 10번이다.


