source = "a,1,b,1,c,1,a,1,d,1,f,1,c,1,apple,6,a,3,b,3"
#data = [['a', 1],['b', 1]['c', 1].....] 중복 허용
list_source = source.split(',')
data = []

for i in range(len(list_source)):
    if i % 2 == 1:
        data.append([list_source[i-1], int(list_source[i])])

print(data)
print('-' * 50)
data2 = []
for j in range(len(data)):
    # 중복여부를 확인하고
    is_dupl = False
    # 중복되는 인덱스 번호를 알아야한다
    for k in range(len(data2)):     #data2 는 늘어나고 모든 data2에 대해서 모든 data 를 대조해봄
        if data2[k][0] == data[j][0]:   #중복값 있음
            is_dupl = True
            no_dupl = k

    if is_dupl:                                     #중복값 있을때
        sum = data[j][1] + data2[no_dupl][1]        #새로운값과 기존의 값을 더함 [1]은 숫자 부분
        data2[no_dupl][1] = sum                     #index k 에다가 sum 값 더함
    else:                                           #중복값 없을때
        data2.append(data[j])                       #append
print(data2)


#1번을 받아들인다