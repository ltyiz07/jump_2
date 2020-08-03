f = open("c:\\pyth\\test_01.txt", 'w')
words = """Life is like an orange - colored tunnel
hahaha
You are always my orange"""
f.write(words)
f.close()


f = open("c:\\pyth\\test_01.txt", 'r')
data = f.read()
f.close()


changed_data = data.replace("orange", "blue")
print(changed_data)

f = open("c:\\pyth\\test_01.txt", 'w')
f.write(changed_data)
f.close()
