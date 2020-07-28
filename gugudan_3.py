#모든 '3'을 '*'으로 출력
#gugudan 과의 다른점은 gugudan은 단순히 "3"만을 if == 3 으로 확인해 줄력하는 반면
#gugudan_3은 모든 출력에서 '3'을 모두 검사해 '3'일때 '*' 출력.
f = open("c:\\pyth\\gugudan_3to_star.txt", 'w')
data = ''
for i in range(1, 10, 1):
    for j in [2, 3, 4]:
        count = 0
        data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
        for k in data:
            if k == '3':
                data = data[:count] + '*' + data[count + 1 :]
            count = count + 1
        f.write(data)
    f.write("\n")
f.write("\n")
f.write("-" * 50)
f.write("\n")
print(len(data))
for i in range(1, 10, 1):
    for j in [5, 6, 7]:
        count = 0
        data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
        for k in data:
            if k == '3':
                data = data[:count] + '*' + data[count + 1:]
            count = count + 1
        f.write(data)
    f.write("\n")
f.write("\n")
f.write("-" * 50)
f.write("\n")

for i in range(1, 10, 1):
    for j in [8, 9]:
        count = 0
        data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
        for k in data:
            if k == '3':
                data = data[:count] + '*' + data[count + 1:]
            count = count + 1
        f.write(data)
    f.write("\n")
f.write("\n")

