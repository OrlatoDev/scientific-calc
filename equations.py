from Calc import Calc
from sympy import solve, sympify, Eq, pretty_print

class Equations(Calc):
    def solve(self, eq):
        try:
            pretty_print(eval(eq))
        except:
            l = sympify(str(eq[:eq.rfind("=")]).strip())
            r = sympify(str(eq[eq.rfind("=") + 1:]).strip())

            result = solve(Eq(l, r), dict = True)
            if len(result) <= 1:
                pretty_print(result[0])
            else:
                pretty_print(result)