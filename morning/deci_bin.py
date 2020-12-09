def deci_to_bin(deci):
    answer = ""

    def to_bin(deci):
        nonlocal  answer
        if deci == 0:
            return
        elif deci % 2 == 1:
            answer += '1'
        else:
            answer += '0'
        to_bin(deci // 2)
    to_bin(deci)
    return answer[::-1]

# very good I think
def to_bin1(deci):
    if deci == 0:
        return ""
    return to_bin1(deci // 2) + str(deci % 2)


def to_tri(deci):
    int_n = int(deci)
    if deci == 0:
        return ""
    return to_tri(int_n // 3) + str(int_n % 3)

def tri_to_deci(n):
    answer = 0
    for e, i in enumerate(n[::-1]):
        num = int(i)
        answer = answer + (3 ** e) * num
    return answer


if __name__ == "__main__":
    # number = input("input deci number ")
    # print(deci_to_bin(int(number)))

    # print(to_bin1(17))
    print(tri_to_deci(to_tri("100")))