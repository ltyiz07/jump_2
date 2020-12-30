# 글자수가 제각각이라 리스트를 사용하면 편할 것같으니깐 문자열들을 리스트 형식으로 바꾸어준다
# 입력되는 문자열의 특징은 각각이 ','로 나뉘어 있다는 것인데
# 리스트 함수중 split을 사용하면된다
# 위의 데이터는 일단 연습이니 코드안에서 정의해준다
source ="""\
apple,2,grape,1,pineapple,1,apple,1,\
tomato,2,grape,1,pineapple,2,apple,1,grape,1\
"""    # 초기의 데어터


list_s = source.split(',')
print(list_s)    # list_s 를 화면에 출력해보면 리스트형으로 전환된것을 확인할 수 있다


data_1 = []    # [문자, 숫자] 쌍이 담길 2차원 리스트
# 그리고 데이터들을 다루기 편하도록 2차원리스트 [문자, 숫자]쌍으로 변환해준다
for i in range(len(list_s)):
    if i % 2 == 0:    # 짝수번째 인덱일때
        # append 함수를 사용하면 리스트에 추가할 수 있다
        data_1.append([list_s[i], int(list_s[i + 1])])    # append 로 추가


# data_2에 for, in문으로 단어들을 담고 담은 단어들을 모두 비교해서 중복을 체크한다
data_2 = []    # 중복처리과정이 끝난 데이터가 담길 리스트
for i in range(len(data_1)):
    # 중복여부를 확인.
    is_dupl = False    # 랫치처럼 중복값이 있을때만 추가하려고 False로 비교할때마다 리셋
    no_dupl = None
    # 중복되는 인덱스 번호를 알아야 한다
    for j in range(len(data_2)):    # data_2의 갯수만큼 반복 실행
        if data_2[j][0] == data_1[i][0]:    # 과일의 종류가 같다면 실행
            is_dupl = True    # 랫치 True
            no_dupl = j    # 인덱스값 저장
    if is_dupl:    # 랫치가 중복값이 있어 True 일때 실행
        sum_fruite = data_1[i][1] + data_2[no_dupl][1]    # 갯수 더하기
        data_2[no_dupl][1] = sum_fruite    # 그값 다시 넣기
    else:
        data_2.append(data_1[i])    # 중복되는 과일이 없으면 리스트에 추가하기


print(data_2)
