

def decoding(c):
    count = 0

    def decode(code):
        nonlocal count
        if len(code) == 0:
            count += 1
            return
        elif len(code) == 1:
            count += 1
            return

        decode(code[1:])
        print(chr(int(code[0]) + 64), end="")
        if int(code[:2]) < 27:
            print(chr(int(code[:2]) + 64), end="")
            decode(code[2:])
        return code

    black_list = []
    for e, ca in enumerate(c):
        if ca == '0':
            black_list.append(e)
    for b in black_list:
        c = c[:e] + c[e + 2:]
    decode(c)
    return count

def encode(word):
    answer = ""
    for w in word:
        answer += str(ord(w) - 64)
    return answer

if __name__ == "__main__":
    code = "91215225251521"
    print(decoding(code))
    print(encode("ILOVEYOU"))


    