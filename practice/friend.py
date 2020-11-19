myfriends = {'a': '가,나', 'b': '다,라,마', 'c': '가,다,바'}

# 친구 명수 확인
how_many = myfriends.values()
print(how_many)
b = set([])
for i in how_many:
    a = i.split(',')
    b = b | set(a)

print("친구 수: ", len(b))

# 순서정렬위해 리스트로 지정
c = list(b)
c.sort()

# value 들 리스트로 변환
for i in myfriends.keys():
    myfriends[i] = myfriends[i].split(',')

for i in c:
    home = []
    for j in myfriends.keys():
        if i in myfriends[j]:
            home.append(j)
    print(i, '=', home)
