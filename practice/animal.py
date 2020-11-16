class Tiger:
    def __init__(self):
        self.food = 0

    def bark(self):
        if self.food > 2:
            print("KKWWKWKWKWW")
            self.food -= 1
        else:
            print("WWoooWWW")

    def feed(self):
        self.food += 1


class Lion:
    def __init__(self):
        self.food = 0

    def bark(self):
        print("KWoooowWWWW")


ellen = Tiger()
mike = Tiger()
ellen.bark()
