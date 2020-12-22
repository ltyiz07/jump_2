def to_hex(num):
    binary = bin(num)
    binary = binary[2:]
    while len(binary) < 8:
        binary = '0' + binary
    first = binary[:4]
    second = binary[4:]
    print(binary)
    print(first, second)
    return first, second




if __name__ == "__main__":
    # with open("./example/example_1.edb", 'br') as file:
    #     a = file.readline()
    #     for i in range(9, 17):
    #         print(bin(a[i]))
    pass
