from practice import *


with open("./example/example_1.edb", 'br') as file:
    a = file.readline()
    for i in a:
        to_hex(i)
        # print(bin(i))
