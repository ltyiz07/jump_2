f = open("D:\\test\\test_01.txt", 'w', encoding='utf8')
for i in range(1, 11):
    f.write("{0:>2} fight the feeling\n".format(i))

f.close()


f = open("D:\\test\\test_01.txt", 'r')

a = f.readlines()
print(a[2][1])
print(type(a))
print(len(a))

f.close()
print("file closed")