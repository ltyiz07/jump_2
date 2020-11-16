#string과 string함수, 포맷만을 사용한 mysum
data = "apple,1,banana,2,apple,4,kiwi,5,apple,3"

index = 0
str = ""
old_str = ""
# 데이터 저장소
name = ""
sums = ""

# 상품목록 추출
for i in data:
    str = str + i
    # print(i,index, str)
    if i == ",":
        if index % 2 == 0:
            # 새로운 상품만 추가
            if name.find(str[:-1]) == -1:
                name = "{0}{1:<10}".format(name,str[:-1])
                sums = "{0}{1:>10}".format(sums,"0")
        # else:
        #     print(index, old_str, "에 값을 더한다.",str)
        old_str = str
        index = index + 1
        str = ""

print("="*50)
print("name: %s" % name)
print("sums: %s" % sums)

# 상품 수량 더하기
index = 0
str = ""
old_str = ""
l = 0

for i in data:
    str = str + i
    l = l + 1
    # print(i,index, str)
    if i == ",":
        if index % 2 == 1:
            print("%s에 %s 더한다." % (old_str[:-1], str[:-1]))
            name_index = name.find(old_str[:-1])
            sub = int(sums[name_index:name_index+10])
            sums = sums[:name_index]+"{0:>10}".format(sub+int(str[:-1]))+sums[name_index+10:]

        old_str = str
        index = index + 1
        str = ""
    elif l == len(data):
        print("last 아이템")
        name_index = name.find(old_str[:-1])
        sub = int(sums[name_index:name_index + 10])
        sums = sums[:name_index] + "{0:>10}".format(sub + int(str)) + sums[name_index + 10:]

print("="*50)
print("name: %s" % name)
print("sums: %s" % sums)
