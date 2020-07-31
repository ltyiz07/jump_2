# 계산기 수를 입력받고 이를 계산
# input = "<연산>"+"<다섯자리수>"
def calc():
    ans = 0
    a = ''
    while True:
        a = input("입력:")
        if a == '':
            continue
        elif a == 'q':
            break
        elif a[0] == '=':
            print(ans)
        elif a[0] == '+':
            ans = ans + int(a[1:])
        elif a[0] == '-':
            ans = ans - int(a[1:])
        elif a[0] == '/':
            ans = ans / int(a[1:])
        elif a[0] == '*':
            ans = ans * int(a[1:])
        else:
            ans = int(a)
    print("ans = ", ans)
# "in" 사용해서 다시 만들어보기
# ex) + in a True

calc()
