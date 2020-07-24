word = "a,4,b,6,d,8,a,8,b,4,c,7,g,9,h,1,a,6,b,3,h,5"

sum_a = 0
sum_b = 0
sum_c = 0
sum_d = 0
sum_e = 0
sum_f = 0
sum_g = 0
sum_h = 0

even = 0
uneven = 1
even = even + 2
uneven = uneven + 2

count = 0

for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    for i in word:
        count = 0
        if count % 4 == 0:
            if i == j:
                sum_a = sum_a + int(word[count + 2])
            if i == j:
                sum_b = sum_b + int(word[count + 2])
            if i == j:
                sum_c = sum_c + int(word[count + 2])
            if i == j:
                sum_d = sum_d + int(word[count + 2])
            if i == j:
                sum_e = sum_e + int(word[count + 2])
            if i == j:
                sum_f = sum_f + int(word[count + 2])
            if i == j:
                sum_g = sum_g + int(word[count + 2])
            if i == j:
                sum_h = sum_h + int(word[count + 2])
        count = count + 1


print(sum_a)
print(sum_b)
print(sum_c)
print(sum_d)
print(sum_e)
print(sum_g)
print(sum_h)

