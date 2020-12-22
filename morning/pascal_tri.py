def pascal_triangle(n):
    answer = []

    def tri(answer, n=0):
        if n == 0:
            return
        elif answer == []:
            answer.append([1])
            tri(answer, n-1)
        elif len(answer) == 1:
            answer.append([1, 1])
            tri(answer, n-1)
        else:
            temp = []
            temp.append(1)
            for a, b in zip(answer[-1][:-1], answer[-1][1:]):
                temp.append(a + b)
            temp.append(1)
            answer.append(temp)
            tri(answer, n-1)
    tri(answer, n)
    return answer


def beauti_print(lst):
    full_length = len(lst)
    for l in lst:
        full_length -= 1
        print(" " * full_length, end="")
        for e in l:
            print(e, end=" ")
        print()


if __name__ == "__main__":
    beauti_print(pascal_triangle(5))
