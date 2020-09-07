class Calc:
    def set_calc(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b


    def sub(self):
        return self.a - self.b


    def div(self):
        return self.a / self.b


    def mult(self):
        return self.a * self.b



class MoreCalc(Calc):
    def div(self):
        if self.b == 0:
            print("don't do that")
            return "I said don't do that"
        else:
            return self.a /self.b

if __name__ == "__main__":

    my_calc_1 = Calc()
    my_calc_2 = Calc()
    my_calc_3 = MoreCalc()


    my_calc_1.set_calc(5, 7)
    my_calc_2.set_calc(12, 7)
    my_calc_3.set_calc(5, 0)
    print(my_calc_1.add())
    print(my_calc_2.sub())
    print(my_calc_3.div())
