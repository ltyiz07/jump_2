#숫자 "3"들만 '*'로 출력 되도록 함.
#
#
f = open("d:\\test\\gugudan_single3finder.txt", 'w')

for i in range(1, 10, 1):
    for j in [2, 3, 4]:
        if j == 3:
            if i == 3:
                data = " * x  * = {2:>2}     ".format(j, i, j * i)
                f.write(data)
            else:
                if i * j == 3:
                    data = " * x {1:>2} =  *     ".format(j, i, j * i)
                    f.write(data)
                else:
                    data = " * x {1:>2} = {2:>2}     ".format(j, i, j * i)
                    f.write(data)
        else:
            if i == 3:
                data = "{0:>2} x  * = {2:>2}     ".format(j, i, j * i)
                f.write(data)
            else:
                print("{0:>2} x {1:>2} = {2:>2}".format(j, i, j * i))
                data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
                f.write(data)
    f.write("\n")
f.write("\n")
f.write("-" * 50)
f.write("\n")

for i in range(1, 10, 1):
    for j in [5, 6, 7]:
        if j == 3:
            if i == 3:
                data = " * x  * = {2:>2}     ".format(j, i, j * i)
                f.write(data)
            else:
                data = " * x {1:>2} = {2:>2}     ".format(j, i, j * i)
                f.write(data)
        else:
            if i == 3:
                data = "{0:>2} x  * = {2:>2}     ".format(j, i, j * i)
                f.write(data)
            else:
                print("{0:>2} x {1:>2} = {2:>2}".format(j, i, j * i))
                data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
                f.write(data)
    f.write("\n")
f.write("\n")
f.write("-" * 50)
f.write("\n")

for i in range(1, 10, 1):
    for j in [8, 9]:
        if j == 3:
            if i == 3:
                data = " * x  * = {2:>2}     ".format(j, i, j * i)
                f.write(data)
            else:
                data = " * x {1:>2} = {2:>2}     ".format(j, i, j * i)
                f.write(data)
        else:
            if i == 3:
                data = "{0:>2} x  * = {2:>2}     ".format(j, i, j * i)
                f.write(data)
            else:
                print("{0:>2} x {1:>2} = {2:>2}".format(j, i, j * i))
                data = "{0:>2} x {1:>2} = {2:>2}     ".format(j, i, j * i)
                f.write(data)
    f.write("\n")
f.write("\n")

