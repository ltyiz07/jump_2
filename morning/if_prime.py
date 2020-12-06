def is_prime_num(num, lst=[]):
    for i in range(2, num):
        if num % i == 0:
            print(i)
            lst.append(i)
            return is_prime_num(int(num / i), lst)
    return num, lst


# def is_prime(num):
#     if num == is_prime_num(num):
#         return "it is prime"
#     else: return is_prime_num(num)
#
#
# from math import sqrt
# def is_prime(num):
#     for j in range(2, int(sqrt(num) + 1)):
#         if num % j == 0:
#             return False
#     return True

def get_prime(num):
    answer = []

    def divider(n):
        for i in range(2, n):
            if n % i == 0:
                answer.append(i)
                print(i)
                return divider(int(n / i))
        answer.append(n)
        return
    divider(num)
    return answer


if __name__ == "__main__":
    # print(is_prime_num(5541566351), a)
    # print("*" * 50)
    # print(is_prime_num(20), b)
    print("*" * 50)
    print(get_prime(51))
