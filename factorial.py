from Calc import Calc

class Factorial(Calc):
    def factorial(self, x):
        result = 1
        
        for i in range(1, x + 1):
            result *= i

        return result