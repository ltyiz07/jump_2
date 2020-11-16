#menian, 중위값 찾기
a = "5,7,4,9,6,3,15"
b = "5,7,4,9,6,3,15,21"
list_a = a.split(',')
list_b = b.split(',')
print(list_a, list_b)
numbers_a = []
numbers_b = []

# listing
for i in list_a:
    numbers_a.append(int(i))
for j in list_b:
    numbers_b.append(int(j))

numbers_a.sort()
numbers_b.sort()            # sorting
print(numbers_a, numbers_b)


def median(listed_numbers):
    lenth = len(listed_numbers)
    if lenth % 2 == 1:
        index = int((lenth - 1) / 2)
        median = listed_numbers[index]
    elif lenth % 2 == 0:
        index_1 = int(lenth / 2)
        index_2 = int(lenth / 2 - 1)
        median = (listed_numbers[index_1] + listed_numbers[index_2]) / 2
    return median


print(median(numbers_a), median(numbers_b))

# soft copy, hard copy 의 차이점 공부해보기