import random               # random import


people = int(input("몇명인가요? :"))

list_people = []
count = 1
for i in range(people):
    list_people.append(count)
    count += 1

sampled_list_people = random.sample(list_people, 5)

for i in range(5):
    print("자동차 당첨({0}등)!! : ".format(6 - i), sampled_list_people[i],  "             계속하려면 enter")
    input()

print("!!빌딩 당첨(1등)!! : ", sampled_list_people[4])