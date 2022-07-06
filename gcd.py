from Calc import Calc

class GCD(Calc):
    def calc(self, *args):
        for i in args[0]: args[0][args[0].index(i)] = int(args[0][args[0].index(i)])

        return args[0]