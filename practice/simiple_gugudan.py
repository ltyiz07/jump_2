f = open("gugudan.txt", 'w')

for i in range(1, 10, 1):
    for j in [2, 3, 4]:
        data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
        f.write(data)
    f.write("\n")
f.write("\n")
f.write("-" * 50)
f.write("\n")

for i in range(1, 10, 1):
    for j in [5, 6, 7]:
        data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
        f.write(data)
    f.write("\n")
f.write("\n")
f.write("-" * 50)
f.write("\n")

for i in range(1, 10, 1):
    for j in [8, 9]:
        data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
        f.write(data)
    f.write("\n")
f.write("\n")
