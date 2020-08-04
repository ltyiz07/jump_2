class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return  self.result

    def show(self):
        print(self.result)

class ComplexCalculator(Calculator):
    def mult(self, num):
        self.result *= num
        return self.result


apple = Calculator()
grape = Calculator()
banana = Calculator()
kiwi = ComplexCalculator()

apple.add(5)
grape.add(20)
banana.add(3)
kiwi.add(10)

apple.sub(1)
grape.sub(1)
banana.add(1)
kiwi.mult(2)

apple.show()
banana.show()
grape.show()
kiwi.show()
