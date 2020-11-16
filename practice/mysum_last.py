#만일 위에서 쓴 폰트를 아래의 콘솔에서도 쓰러면 import 사용
#콘솔에서
#import "파일명"
#ex200727.source
#리스트 2차원으로 사용

source = "a,1,b,2,c,3,a,1,d,2,c,3,a,5,b,2,b,2,a,1,d,1"
temp = source.split(",")
data = []
data2 = []
# for i in temp:
# len(temp)는 12
# temp가 12개 이므로 range(len(temp))
# 0,1,2 ... , 10,11을 만든다
# for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
for i in range(len(temp)):
    sub_list = []
    if i%2 == 1:
        sub_list.append(temp[i-1])
        sub_list.append(int(temp[i]))
        data.append(sub_list)

for i in range(len(data)):
    # 반복문으로 중복인지만 판다
    is_dupl = False
    for j in range(len(data2)):
        if data2[j][0] == data[i][0]:       #중복 있음
            is_dupl = True
            no_dupl = j
    if is_dupl:
        # 값을 더한다.
        sum = data2[no_dupl][1] + data[i][1]
        data2[no_dupl][1] = sum
    else:
        data2.append(data[i])

print(data2)
