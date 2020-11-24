with open(".\\example_files\\reader.txt", 'r', encoding="utf-8") as f:

    a = "start"
    while a != "":
        a = f.readline()
        print(a)


