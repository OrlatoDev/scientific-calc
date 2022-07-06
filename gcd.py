from Calc import Calc
from lcm import LCM

class GCD(Calc):
    def calc(self, *args):
        for i in args[0]: args[0][args[0].index(i)] = int(args[0][args[0].index(i)])

        lcm = LCM()

        p = 1
        for i in args[0]:
            p *= i
        
        return p / lcm.calc(args[0])
