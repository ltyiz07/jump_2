class Counter:
    def __init__(self):
        self.files = []
        self.folder_name = ""
        self.first_line = []
        self.second_line = []
        self.fruits = []
        self.numbers = []

# input 으로 /fruit_shop 내부의 폴더 를 지정해주면 내부의 파일들을 읽어서 리스트로 변환
    def file_finder(self, folder_name):
        self.folder_name = folder_name
        import os
        files = os.scandir("%s" % folder_name)
        for file in files:
            self.files.append(file.name)

# 읽어온 파일들의 첫째줄, 둘째줄을 가져옴
    def file_reader(self):
        for i in self.files:
            with open("{0}/{1}".format(self.folder_name, i), 'r') as f:
                first_line = f.readline()
                second_line = f.readline()
                self.first_line.append(first_line)
                self.second_line.append(second_line)

    def sorting(self):
        for i in self.second_line:
            listed_data = i.split(',')
            for j in range(int(len(listed_data) / 2)):
                if self.fruits.count(listed_data[2 * j]) > 0:
                    self.numbers[self.fruits.index(listed_data[2 * j])] = int(self.numbers[self.fruits.index(listed_data[2 * j])]) + int(listed_data[2 * j + 1])
                else:
                    self.fruits.append(listed_data[2 * j])
                    self.numbers.append(int(listed_data[2 * j + 1]))
        print(self.fruits)
        print(self.numbers)

    def writing(self):
        with open("{0}".format("{0}.txt").format(self.folder_name),'w') as f:
            for i in range(len(self.fruits)):
                a = "{0:<10}: {1:<2}\n".format(self.fruits[i], self.numbers[i])
                f.write(a)


if __name__ == "__main__":
    test = Counter()
    test.file_finder("fruit_shop")
    test.file_reader()

    print(test.folder_name)
    print(test.files)

    test.sorting()
    test.writing()

    run = Counter()
    run.file_finder("fruit_banch")
    run.file_reader()
    run.sorting()
    run.writing()