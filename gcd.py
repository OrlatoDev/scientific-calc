from Calc import Calc

class GCD(Calc):
    def calc(self, *args):
        for i in args[0]: args[0][args[0].index(i)] = int(args[0][args[0].index(i)])

        def findgcd(x, y):
            while(y):
                x, y = y, x % y
            
            return x

        n1 = args[0][0]
        n2 = args[0][1]

        gcd = findgcd(n1, n2)
        for i in range(2, len(args[0])):
            gcd = findgcd(gcd, args[0][i])

        return gcd
