import datetime
today = datetime.datetime.today()
<<<<<<< HEAD
#month = today.month
#day = today.day
=======
# month = today.month
# day = today.day
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e

month = 7
day = 16


<<<<<<< HEAD
#모든 수에대한 큰이미지 수 지정
num0 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") +  "{0:5}\n".format("#   #") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("")
print(num0)
num1 = "{0:5}\n".format("    #") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num1)
num2 = "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:#^5}\n".format("") + "{0:5}\n".format("#    ") + "{0:#^5}\n".format("")
print(num2)
num3 = "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:#^5}\n".format("")
print(num3)
num4 = "{0:5}\n".format("#   #") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num4)
num5 = "{0:#^5}\n".format("") + "{0:5}\n".format("#    ") + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:#^5}\n".format("")
print(num5)
num6 = "{0:5}\n".format("#    ") + "{0:5}\n".format("#    ") + "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("")
print(num6)
num7 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:5}\n".format("#   #") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num7)
num8 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("")
print(num8)
num9 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num9)
num10 = "{0:7}\n".format("# #####") + "{0:7}\n".format("# #   #") + "{0:7}\n".format("# #   #") + "{0:7}\n".format("# #   #") + "{0:7}\n".format("# #####")
print(num10)
num11 = "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #")
print(num11)
num12 = "{0:7}\n".format("# #####") + "{0:7}\n".format("#     #") + "{0:7}\n".format("# #####") + "{0:7}\n".format("# #    ") + "{0:7}\n".format("# #####")
=======
# 모든 수에대한 큰이미지 수 지정
num0 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #")\
       + "{0:5}\n".format("#   #") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("")
print(num0)
num1 = "{0:5}\n".format("    #") + "{0:5}\n".format("    #")\
       + "{0:5}\n".format("    #") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num1)
num2 = "{0:#^5}\n".format("") + "{0:5}\n".format("    #")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("#    ") + "{0:#^5}\n".format("")
print(num2)
num3 = "{0:#^5}\n".format("") + "{0:5}\n".format("    #")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:#^5}\n".format("")
print(num3)
num4 = "{0:5}\n".format("#   #") + "{0:5}\n".format("#   #")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num4)
num5 = "{0:#^5}\n".format("") + "{0:5}\n".format("#    ")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:#^5}\n".format("")
print(num5)
num6 = "{0:5}\n".format("#    ") + "{0:5}\n".format("#    ")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("")
print(num6)
num7 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #")\
       + "{0:5}\n".format("#   #") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num7)
num8 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("#   #") + "{0:#^5}\n".format("")
print(num8)
num9 = "{0:#^5}\n".format("") + "{0:5}\n".format("#   #")\
       + "{0:#^5}\n".format("") + "{0:5}\n".format("    #") + "{0:5}\n".format("    #")
print(num9)
num10 = "{0:7}\n".format("# #####") + "{0:7}\n".format("# #   #")\
        + "{0:7}\n".format("# #   #") + "{0:7}\n".format("# #   #") + "{0:7}\n".format("# #####")
print(num10)
num11 = "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #")\
        + "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #") + "{0:7}\n".format("  #   #")
print(num11)
num12 = "{0:7}\n".format("# #####") + "{0:7}\n".format("#     #")\
        + "{0:7}\n".format("# #####") + "{0:7}\n".format("# #    ") + "{0:7}\n".format("# #####")
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
print(num12)

print('=' * 50)

<<<<<<< HEAD
#숫자들 편하게 가져오기
numbers = (num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12)

#파일 생성
f = open("D:\\test\\daybyday.txt", 'w')

#month printing
if month // 10 == 0:
    print(numbers[month],"\n")
=======
# 숫자들 편하게 가져오기
numbers = (num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12)

# 파일 생성
f = open("D:\\test\\daybyday.txt", 'w')

# month printing
if month // 10 == 0:
    print(numbers[month], "\n")
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
    data = numbers[month] + "\n"
    f.write(data)
else:
    rest_ten = month % 10
    print(numbers[1], "\n", numbers[rest_ten], "\n")
    data = numbers[month] + "\n"
    f.write(data)

<<<<<<< HEAD
#middle_bar printing
print("{0:#^5}\n".format("    #") + "{0:#^5}\n".format("   # ") + "{0:#^5}\n".format("  #  ") + "{0:#^5}\n".format(" #   ") + "{0:#^5}\n".format("#    "))
data = "{0:#^5}\n".format("    #") + "{0:#^5}\n".format("   # ") + "{0:#^5}\n".format("  #  ") + "{0:#^5}\n".format(" #   ") + "{0:#^5}\n".format("#    ") + '\n'
f.write(data)

#day printing

#over 29 days
#
=======
# middle_bar printing
print(""""{0:#^5}\n".format("    #") + "{0:#^5}\n".format("   # ")
 + "{0:#^5}\n".format("  #  ") + "{0:#^5}\n".format(" #   ") + "{0:#^5}\n".format("#    ")""")
data = "{0:#^5}\n".format("    #") + "{0:#^5}\n".format("   # ")\
       + "{0:#^5}\n".format("  #  ") + "{0:#^5}\n".format(" #   ") + "{0:#^5}\n".format("#    ") + '\n'
f.write(data)

print("=" * 100)
print(type(f))
print(type(10))
print("=" * 100)
# day printing

# over 29 days
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
if day > 29:
    data = numbers[3] + "\n"
    f.write(data)
    rest_day = day % 30
    data = numbers[rest_day] + "\n"
    f.write(data)

if day > 19:
<<<<<<< HEAD
    if day <30:
=======
    if day < 30:
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
        data = numbers[2] + "\n"
        f.write(data)
        rest_day = day % 20
        data = numbers[rest_day] + "\n"
        f.write(data)

if day > 9:
<<<<<<< HEAD
    if day <20:
=======
    if day < 20:
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
        data = numbers[1] + "\n"
        f.write(data)
        rest_day = day % 10
        data = numbers[rest_day] + "\n"
        f.write(data)

if day > 0:
<<<<<<< HEAD
    if day <10:
=======
    if day < 10:
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
        rest_day = day % 10
        data = numbers[rest_day] + "\n"
        f.write(data)


<<<<<<< HEAD

f = open("D:\\test\\daybyday.txt", 'a')

f.close()
=======
f = open("D:\\test\\daybyday.txt", 'a')

f.close()
>>>>>>> b2955f0282ff77dbcb8789c7efdb099f956a6a2e
