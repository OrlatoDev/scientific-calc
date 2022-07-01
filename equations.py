from Calc import Calc
from sympy import solve, sympify, Eq, pretty_print, symbols

class Equations(Calc):
    def solve(self, eq):
        try:
            result = solve(Eq(sympify(str(eq)), symbols("x")), dict = True)

            if len(result) <= 1:
                pretty_print(result[0])
            else:
                pretty_print(result)
        except:
            try:
                l = sympify(str(eq[:eq.rfind("=")]).strip())
                r = sympify(str(eq[eq.rfind("=") + 1:]).strip())

                result = solve(Eq(l, r), dict = True)
                if len(result) <= 1:
                    pretty_print(result[0])
                else:
                    pretty_print(result)  
            except:
                self.print_error("Invalid syntax...")
