#만일 위에서 쓴 폰트를 아래의 콘솔에서도 쓰러면 import 사용
#콘솔에서
#import "파일명"
#ex200727.source
#리스트 2차원으로 사용

source = "a,1,b,2,c,3,a,1,d,2,c,3"
temp = source.split(",")
data = []

for i in range(len(temp)):
    sub_list = []
    if i%2 == 1:
        sub_list.append(temp[i-1])
        sub_list.append(temp[i])
        data.append(sub_list)
    print(sub_list)

print(data)


