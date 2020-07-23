#먼저 입력할 단어의 갯수를 입력
#수만큼의 단어를 입력
#R 기준으로 반으로 나뉨(모든 단어에는 R포함)

count = 0
words = "20010131Rainy", "179Rai354ny", "21R354yn76"


in_words = ["1", "2", "3", "4", "5", "6", "7"]

for i in range(7):
    in_words[i] = input("press any key: ")

R_count = 0

for i in in_words:
    count = 0
    for j in i:
        if j == 'R':
            R_count = count
        count = count + 1
    print("A: ", i[:R_count])
    print("B: ", i[R_count:])

print(type(in_words))