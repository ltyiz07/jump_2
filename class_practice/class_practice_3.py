class FourCal:
    j = 4

    def setdata(self, a, b):
        self.c = a
        self.b = b
        print(a, b)
        return(a)


    def add(self):
        return self.c + self.b


obj1 = FourCal()
obj1.setdata(4, 2)
print(obj1.setdata(3, 4))
print(obj1.c)
print(obj1.add())
obj2 = FourCal()
obj2.setdata(3, 7)
print(obj2.add())

obj1.setdata(2, 3)
FourCal.j = 7
# a.add()
# a.sub()
# a.mul()
# a.div()