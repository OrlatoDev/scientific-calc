from mimetypes import init
from Calc import Calc
from sympy import solve, sympify, Eq, pretty_print

class Equations(Calc):
    def solve(self, eq):
        l = sympify(str(eq[:eq.rfind("=")]).strip())
        r = sympify(str(eq[eq.rfind("=") + 1:]).strip())

        pretty_print(solve(Eq(l, r), dict = True))