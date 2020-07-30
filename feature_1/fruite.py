import os


def read_data(param):       # 매개변수: 주소, 리턴: 첫째줄, 둘째줄
    with open(param, 'r', encoding="utf8") as f:
        line_1 = f.readline()
        line_2 = f.readline()
        return line_1, line_2


# 스트링을 2차원 리스트로 변환
def listing(*sale):     # 매개변수: 문자열"단어,단어,단어..." 리턴: 리스트 ["단어","단어","단어",...]
    data = []
    for m in range(len(sale)):
        list_sale = sale[m].split(',')
        data.append(list_sale)
    return data


# 2차원 리스트의 각 1번인덱스값 즉 숫자를 str 에서 int 로 변환
def sorting(listed_data_in_sorting):
    data2 = []
    for n in range(len(listed_data_in_sorting)):
        for j in range(len(listed_data_in_sorting[n])):
            if (j % 2) == 0:
                data2.append([listed_data_in_sorting[n][j], int(listed_data_in_sorting[n][j + 1])])
    return data2


# 중복을 없에고 각 중복된 수들을 모두 더해줌
def adding(sorted_data):
    data3 = []
    for k in range(len(sorted_data)):
        is_dupl = False
        for j in range(len(data3)):
            if data3[j][0] == sorted_data[k][0]:
                data3[j][1] = data3[j][1] + sorted_data[k][1]
                is_dupl = True
                break
        if not is_dupl:
            data3.append(sorted_data[k])
    return data3


all_data = ""
with os.scandir("D:\\leety\\Desktop\\trials\\sales") as entries:
    for entry in entries:
        person, sale_data = read_data("D:\\leety\\Desktop\\trials\\sales\\{0}".format(entry.name))
        print(sale_data)
        all_data = all_data + sale_data + ","       # 여기서 문자열 마지막에 불필요한 ',' 발생
print("all_data:", all_data)

if __name__ == "__main__":          # 더 알아보기
    listed_data = listing(all_data)   # 리스트로 변환하는 함수 사용
    listed_data[0].pop()            # 문자열 더하는 과정에서 생긴 코마 없애기 위해 필요...
    show_data = adding(sorting(listed_data))            # 함수들 한번에 사용...
    print(show_data)            # 확인해보기


    with open("D:\\leety\\Desktop\\trials\\sales.txt", 'w') as f1:
        count = 0
        for i in show_data:
            a = show_data[count][0]
            b = show_data[count][1]
            show = "{0:<10} : {1} \n".format(a, b)
            f1.write(show)
            count += 1


# import feature_1.fruite
#
# feature_1.fruite.adding
#
#
# from feature_1.fruite import adding
# 로 프로젝트 내의 다른 파일에서도 불러올 수 있음
# calc_3.py 에서 참조함
