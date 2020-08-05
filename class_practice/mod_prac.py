from calc_prac import Calc

class PowCalc(Calc):
    def pow(self):
        return self.a ** self.b

triple = PowCalc()
triple.set_calc(4, 2)
print(triple.pow())

import func_1

print(func_1.find_num([1, 2, 3, 4], 2))