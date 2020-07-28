#teacher_mysum.py 리스트 사용해서 재구성하기

#data 는 string 이고 ','로 나뉨
data = "apple,1,banana,2,apple,4,kiwi,5,apple,3,banana,23,tree,2,kiwi,4"
data_list = data.split(',')
word_list = []
num_list = []

count = 0
for i in data_list:
    if (count % 2) == 0:                #짝수는 단어에 대한 이때 이에 해당되는 숫자 index : count + 1
        if word_list.count(i) > 0:              #단어가 이미 있을때
            num_list[word_list.index(i)] = int(num_list[word_list.index(i)]) + int(data_list[count + 1])    #단어에 해당하는 인덱스에 추가
        else:               #단어가 없을때
            word_list.append(i)             #단어 추가
            num_list.append(data_list[count + 1])           #숫자 새로 추가하기

    else: pass              #홀수는 숫자에 대한
    count += 1
count = 0
for i in word_list:
    print(i,":")
    print(num_list[count])
    count += 1