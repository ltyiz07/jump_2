# 표시할 요소를 분해하여 변수로 만든다
df = "*****"
dl = "*    "
dr = "    *"
de = "     "
db = "*   *"

big_font_0 = "%s\n%s\n%s\n%s\n%s" % (df,db,db,db,df)
big_font_1 = "%s\n%s\n%s\n%s\n%s" % (dr,dr,dr,dr,dr)
big_font_2 = "%s\n%s\n%s\n%s\n%s" % (df,dr,df,dl,df)
big_font_3 = "%s\n%s\n%s\n%s\n%s" % (df,dr,df,dr,df)
big_font_4 = "%s\n%s\n%s\n%s\n%s" % (db,db,df,dr,dr)
big_font_5 = "%s\n%s\n%s\n%s\n%s" % (df,dl,df,dr,df)
big_font_6 = "%s\n%s\n%s\n%s\n%s" % (dl,dl,df,db,df)
big_font_7 = "%s\n%s\n%s\n%s\n%s" % (df,db,db,dr,dr)
big_font_8 = "%s\n%s\n%s\n%s\n%s" % (df,db,df,db,df)
big_font_9 = "%s\n%s\n%s\n%s\n%s" % (df,db,df,dr,df)
big_font_d = "%s\n%s\n%s\n%s\n%s" % (de,de,de,de,dr)
big_font_t = "%s\n%s\n%s\n%s\n%s" % (de,de,df,de,de)

big_font = [
    big_font_0, big_font_1, big_font_2, big_font_3, big_font_4, big_font_5,
    big_font_6, big_font_7, big_font_8, big_font_9, big_font_d, big_font_t
]

#날짜 불러오기
#import datetime
#today = datetime.datetime.today()

#today = str(datetime.datetime.today()[0:10])
#print(today)


#month = today.month
#day = today.day
date = "2020-07-24"


#for i in date:
#    if i == "-":
#        print(big_font[11])
#    elif i == ":":
#        print(big_font[10])
#    else:
#        # "2" -> 2
#        i = int(i)
#        print(big_font[i])
print("-" * 50)
####별표 열개...
print(big_font[0][0:5])
print(big_font[0][6:11])
print(big_font[0][12:17])
print(big_font[0][18:23])
print(big_font[0][24:29])


#파일에 쓰기
f = open("D:\\test\\bigtext.txt", 'w')

count = 0
data = ""
great = ""
for i in [0, 1, 2, 3, 4]:
    for j in date:
        if j == '-':
            data = data + big_font[11][6 * count:6 * count + 5] + " "
        elif j == ':':
            data = data + big_font[10][6 * count:6 * count + 5] + " "
        else:
            j = int(j)
            data = data + big_font[j][6 * count:6 * count + 5] + " "
    f.write(data)
    f.write("\n")
    data = ''
    count = count + 1

f.close()
#파일 닫기