from Calc import Calc

class LCM(Calc):
    def calc(self, *args):
        for i in args[0]: args[0][args[0].index(i)] = int(args[0][args[0].index(i)])

        multiples = []

        for i in range(1, max(args[0]) * max(args[0])):
            for j in args[0]:
                multiples.append(i * j)

        multiples.sort()
        for i in multiples:
            if multiples.count(i) == len(args[0]):
                return i
