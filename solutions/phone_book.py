def solution(phone_book):
    length_whole = len(phone_book) - 1
    for i in range(length_whole):
        length_i = len(phone_book[i])
        for p in phone_book[i + 1:]:
            length_p = len(p)
            if length_i <= length_p:
                if phone_book[i] == p[:length_i]:
                    return False
            if length_i > len(p):
                if p == phone_book[i][:length_p]:
                    return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))


def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

import re
def solution(phoneBook):

    for b in phoneBook:
        p = re.compile("^"+b)
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True