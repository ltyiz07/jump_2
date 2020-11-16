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
big_font_t = "%s\n%s\n%s\n%s\n%s" % (de,de,df,de,de)

big_font = [
    big_font_0, big_font_1, big_font_2, big_font_3, big_font_4, big_font_5,
    big_font_6, big_font_7, big_font_8, big_font_9, big_font_t
]


#date = "2002-06-23" 이 라인은 '#'으로 주석처리되어 코드에 반영되지 않는다.
import datetime
now = str(datetime.datetime.today())
date = now[0:10]

print(big_font_0[0:5])
print(big_font_0[6:11])
print(big_font_0[12:17])
print(big_font_0[18:23])
print(big_font_0[24:29])

#파일 열기
f = open("C:\\pyth\\jump_1\\bigtext.txt", 'w')
#파일에 쓸 내용

data_add = ""
count = 0
for i in [0, 1, 2, 3, 4]:
    for j in date:
        if j == '-':
            data = big_font[10][count * 6:count * 6 + 5] + " "
            data_add = data_add + data
        else:
            data = big_font[int(j)][count * 6:count * 6 + 5] + " "
            data_add = data_add + data
    f.write(data_add)
    f.write('\n')
    data_add = ""
    count = count + 1

f.close()
#파일 닫음