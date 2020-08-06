lorem = input("paste words")

count = 0

re_count = 0
for i in lorem:
    count = count + 1
    if i == 'r':
        if lorem[count] == 'e':
            print("RE found")
            re_count = re_count + 1
print(re_count)
